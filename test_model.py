import requests 

# Example packet features (change to your format)
features = [0.0] * 77 # You can modify values here for testing
#features = [1.2] * 77
features = [0.0] * 77

# Duration and traffic burst characteristics
features[0] = 25000.0     # Duration (long session)
features[4] = 8000.0      # Total Fwd Packets (large number of requests)
features[5] = 10000.0     # Total Backward Packets
features[23] = 4000.0     # Fwd Packet Length Mean (unusually large)
features[24] = 3500.0     # Fwd Packet Length Std
features[26] = 1.0        # URG Flag Count
features[27] = 1.0        # ACK Flag Count
features[31] = 800000.0   # Packet Length Variance (large and spiky traffic)
features[42] = 100.0      # Flow Rate (packets/sec)
features[44] = 2000.0     # Active Time
features[45] = 10.0       # Idle Time
features[51] = 20000.0    # Bytes Sent
features[52] = 20000.0    # Bytes Received
features[60] = 50.0       # Flow Duration / Active Ratio
features[62] = 5.0        # Reset Flag Count

# You can optionally randomize some less important ones
import random
for i in range(77):
    if features[i] == 0.0:
        features[i] = round(random.uniform(0.0, 5.0), 2)

response = requests.post("http://127.0.0.1:5000/predict", json={"features": features})

if response.status_code == 200:
    print("✅ Prediction: ", response.json()['prediction'])
else:
    print("❌ Error:", response.json())
