import pickle
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

class AnomalyDetector:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        # Initialize label encoders for categorical features
        self.protocol_encoder = LabelEncoder()
        self.service_encoder = LabelEncoder()
        self.flag_encoder = LabelEncoder()
        # Fit the encoders with the original training data categories
        # These categories should match those used during training
        self.protocol_encoder.fit(['tcp', 'udp', 'icmp'])
        self.service_encoder.fit(['http', 'ftp', 'smtp'])
        self.flag_encoder.fit(['SF', 'S0', 'REJ'])

    def preprocess(self, data):
        # Assume data format: [protocol, service, flag, feature1, feature2, ..., featureN]
        protocol, service, flag, *features = data
        protocol = self.protocol_encoder.transform([protocol])[0]
        service = self.service_encoder.transform([service])[0]
        flag = self.flag_encoder.transform([flag])[0]
        return [protocol, service, flag] + features

    def predict(self, data):
        processed_data = self.preprocess(data)
        print(f"Processed data: {processed_data}")  # Debug output
        return self.model.predict([processed_data])[0]

def test_anomaly_detector():
    model_path = Path('model.pkl')  # Adjust the path if necessary
    detector = AnomalyDetector(model_path)

    # Example test data
    test_data = [
        ['tcp', 'smtp', 'SF', 1592, 372, 1, 1, 0, 147, 0.81],
        # Add more test cases as needed
    ]

    for data in test_data:
        result = detector.predict(data)
        print(f"Input: {data}, Predicted: {result}")  # Output prediction for each input

if __name__ == "__main__":
    test_anomaly_detector()
