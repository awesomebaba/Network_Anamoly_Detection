# Network Anomaly Detection Model - (VidyutKavach)

## Design of CYBER-SECURITY ENABLED SMART CONTROLLER for grid-connected Microgrid

The Network Anomaly Detection Model is part of the VidyutKavach platform, designed to ensure the security of microgrid networks. This model leverages machine learning to identify abnormal network behaviors that may indicate potential security threats or network intrusions. By monitoring real-time network traffic, the system can swiftly detect and respond to anomalies, helping to protect critical infrastructure from cyberattacks and unauthorized access.

## Features
The model analyzes multiple parameters related to network traffic. The following features were selected for final prediction using a Random Forest Classifier (RFC):

protocol_type: Type of communication protocol (e.g., TCP, UDP).

service: The network service being accessed (e.g., HTTP, FTP).

flag: The status of the network connection.

src_bytes: Number of bytes transferred from the source.

dst_bytes: Number of bytes transferred to the destination.

count: Number of connections to the same host within a specific time window.

same_srv_rate: Rate of connections to the same service.

diff_srv_rate: Rate of connections to different services.

dst_host_srv_count: Number of connections to the 
destination host using the same service.

dst_host_same_srv_rate: Percentage of connections to the destination host using the same service.

## Functionality

**Real-time Monitoring**: The model continuously monitors live network traffic and processes the incoming data.

**Anomaly Detection**: The logistic regression model, trained on historical network data, predicts whether the current network activity is normal or anomalous based on the input features.
**Flagging Suspicious Activity**: If the predicted result suggests an anomaly, the system triggers an alert. Depending on the anomaly’s severity, it may block the suspicious traffic or isolate the affected system.

### Tech-Stack -Used : Python, Pandas, Seaborn, MatplotLib, Sk-learn, RFC