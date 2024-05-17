from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from model_loader import load_model
from digit_predictor import predict_digit
from image_formatter import format_image
import time
import os
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Gauge
import psutil

app = FastAPI()
loaded_model = None
ALLOWED_IMAGE_FORMATS = ['png', 'jpeg', 'jpg']  # Allowed image formats

@app.on_event("startup")
async def startup_event():
    global loaded_model
    # Load model on startup
    model_path = "mnist_model.h5"
    loaded_model = load_model(model_path)

# Prometheus metrics
request_counter = Counter("api_requests_total", "Total number of API requests", ["client_ip"])
inference_time_gauge = Gauge("api_inference_time_seconds", "Time taken for inference in seconds")
processing_time_per_char_gauge = Gauge("api_processing_time_per_char_microseconds", "Processing time per character in microseconds")
network_receive_bytes = Gauge("api_network_receive_bytes", "Total network receive bytes")
network_transmit_bytes = Gauge("api_network_transmit_bytes", "Total network transmit bytes")
memory_utilization = Gauge("api_memory_utilization_percent", "API memory utilization in percent")
cpu_utilization = Gauge("api_cpu_utilization_percent", "API CPU utilization in percent")

Instrumentator().instrument(app).expose(app)

@app.post('/predict')
async def predict(request: Request, file: UploadFile = File(...)):
    # Check if the uploaded file is of allowed image format
    if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_IMAGE_FORMATS):
        raise HTTPException(status_code=400, detail="Please upload images of format PNG/JPEG")
    
    client_ip = request.client.host
    request_counter.labels(client_ip=client_ip).inc()

    # Read the bytes from the uploaded image
    contents = await file.read()

    # Convert the image bytes to a 1D array of 784 elements
    data_point = format_image(contents)
    
    start_time = time.time()
    # Predict the digit and its confidence score
    digit, confidence_score = predict_digit(loaded_model, [data_point])
    end_time = time.time()
    
    inference_time = end_time - start_time
    inference_time_gauge.set(inference_time)

    # Get memory and CPU utilization
    memory_utilization.set(psutil.virtual_memory().percent)
    cpu_utilization.set(psutil.cpu_percent())

    # Calculate the effective processing time per character
    input_length = len(contents)  # Use the length of the file contents
    processing_time_per_char = (inference_time * 1e6) / input_length  # Convert to microseconds per character
    processing_time_per_char_gauge.set(processing_time_per_char)

    # Get network I/O bytes
    net_io = psutil.net_io_counters()
    network_receive_bytes.set(net_io.bytes_recv)
    network_transmit_bytes.set(net_io.bytes_sent)
    
    # Return the prediction and confidence score
    return {"digit": digit, "confidence_score": float(confidence_score)}

# Run the app using: uvicorn main:app --reload
