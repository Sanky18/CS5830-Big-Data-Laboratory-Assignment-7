import numpy as np

def predict_digit(model, data_point):
    """
    Predict the digit using the loaded model and serialized data.
    """
    # Make prediction
    probabilities = model.predict(data_point)
    # Get the index of the class with the highest probability
    predicted_class_index = np.argmax(probabilities[0])
    # Get the confidence score of the predicted class
    confidence_score = np.max(probabilities[0])
    # Get the predicted digit (class)
    predicted_digit = int(predicted_class_index)
    return predicted_digit, confidence_score