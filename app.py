from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load saved model, scaler, and label encoder
model = joblib.load('traffic_classifier.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get('features')

    if not features:
        return jsonify({'error': 'No features provided'}), 400

    try:
        scaled = scaler.transform([features])
        pred = model.predict(scaled)
        label = label_encoder.inverse_transform(pred)[0]
        return jsonify({'prediction': label})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    
