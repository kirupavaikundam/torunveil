from sklearn.ensemble import IsolationForest
import pandas as pd

# Train a simple model
def train_model():
    data = pd.DataFrame({
        'packet_size': [500, 300, 450, 800, 1200],
        'time_interval': [0.1, 0.2, 0.15, 0.3, 0.5]
    })
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    return model

model = train_model()

def detect_anomaly(features):
    packet_size = features.get("packet_size")
    time_interval = features.get("time_interval")
    data = [[packet_size, time_interval]]
    prediction = model.predict(data)
    return prediction[0] == -1  # True if anomaly
