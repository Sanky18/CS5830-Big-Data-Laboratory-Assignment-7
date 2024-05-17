import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from io import BytesIO


# Load the MNIST model
model_path = "A:\Jan-May 2024\CS5830-Big Data Laboratory\Assignment-6\\app\mnist_model.h5"
model = load_model(model_path)

def format_image(image_path):
    """
    Resize the uploaded image to 28x28 grayscale, convert it to float32, and normalize the pixel values.
    Returns a 1D array of 784 elements.
    """
    # Open and resize the image
    img = Image.open(image_path).resize((28, 28)).convert('L')
    # Convert image to numpy array, convert to float32, and normalize
    img_array = np.array(img, dtype=np.float32) / 255.0
    # Flatten the array to 1Ds
    img_array = np.array(img_array).reshape(1, -1)
    return img_array

def predict_digit(model, data_point):
    """
    Predict the digit using the loaded model and serialized data.
    """
    # Make prediction
    probabilities = model.predict(data_point)
    predicted_class_index = np.argmax(probabilities, axis=-1)
    confidence_score = probabilities[0][predicted_class_index][0]
    return predicted_class_index[0], confidence_score


# Path to the PNG image file for testing
image_path = "A:\Jan-May 2024\CS5830-Big Data Laboratory\Assignment-6\\tests\\test_digit.png"

# Format the image
data_point = format_image(image_path)

# Predict the digit and confidence score
digit, confidence_score = predict_digit(model, [data_point])

print("Predicted Digit:", digit)
print("Confidence Score:", confidence_score)