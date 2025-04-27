import pyshark
import requests # type: ignore

def extract_features(packet):
    return [len(packet), 0, 1, 0, 1, 1]  # Example only

capture = pyshark.LiveCapture(interface='Wi-Fi')
for packet in capture.sniff_continuously(packet_count=10):
    try:
        features = extract_features(packet)
        response = requests.post("http://localhost:5000/predict", json={"features": features})
        print("Prediction:", response.json())
    except Exception as e:
        print("Error:", e)
        