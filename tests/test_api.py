import requests

# URL of the API endpoint
api_url = "http://127.0.0.1:8000/predict"

# Test uploading and predicting a digit image
def test_predict_digit():
    with open("test_digit.png", "rb") as f:
        file_data = {"file": f}
        response = requests.post(api_url, files=file_data)
        assert response.status_code == 200
        assert "digit" in response.json()