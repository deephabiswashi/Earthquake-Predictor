# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
import pickle
import numpy as np
import time

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all routes

# Load the saved model and scaler
model = tf.keras.models.load_model('notebook/saved_models_scalar/earthquake_model.keras')
with open('notebook/saved_models_scalar/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Predefined dictionary mapping country names (in lowercase) to approximate [latitude, longitude]
country_coords = {
    "usa": [37.0902, -95.7129],
    "india": [20.5937, 78.9629],
    "japan": [36.2048, 138.2529],
    "indonesia": [-0.7893, 113.9213],
    "chile": [-35.6751, -71.5430],
    "turkey": [38.9637, 35.2433]
}

@app.route('/')
def home():
    # Serve the front-end website
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Expect a JSON payload with a "country" field
    data = request.get_json()
    country = data.get('country', '').lower()

    if country not in country_coords:
        error_msg = f"Country not supported. Please try one of: {', '.join(country_coords.keys())}"
        return jsonify({"error": error_msg}), 400

    lat, lon = country_coords[country]
    # Use current Unix timestamp as the time input
    unix_time = time.time()

    # Prepare input: [unix_time, latitude, longitude]
    input_data = np.array([[unix_time, lat, lon]])
    # Scale input using the same scaler used during training
    input_scaled = scaler.transform(input_data)
    # Get prediction from the model
    prediction = model.predict(input_scaled)
    predicted_magnitude = float(prediction[0][0])
    predicted_depth = float(prediction[0][1])

    response = {
        "country": country,
        "predicted_magnitude": predicted_magnitude,
        "predicted_depth": predicted_depth
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
