# IoT Network Intrusion Detection System

## Overview
The IoT Network Intrusion Detection System is a Machine Learning-based application that detects whether network traffic is **Normal** or **Anomalous**. The project uses a trained classification model to analyze network traffic features and predict potential intrusions, helping improve the security of IoT networks.

## Features
- Detects Normal and Anomalous network traffic.
- High-accuracy Machine Learning model.
- User-friendly Streamlit interface.
- Manual feature input for real-time prediction.
- Fast and efficient prediction using a pre-trained model.

## Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Project Structure

```
IoT-Network-Intrusion-Detection/
│── app.py
│── best_model.pkl
│── scaler.pkl
│── label_encoder.pkl
│── requirements.txt
│── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/IoT-Network-Intrusion-Detection.git
cd IoT-Network-Intrusion-Detection
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Usage
1. Launch the Streamlit application.
2. Enter the required network feature values manually.
3. Click the **Predict** button.
4. The application displays whether the network traffic is **Normal** or **Anomaly**.

## Model
The model was trained on an IoT Network Intrusion Detection dataset using Machine Learning techniques with preprocessing, feature scaling, and classification.

## Future Enhancements
- Multi-class attack detection.
- Real-time network traffic monitoring.
- Advanced visualization dashboard.
- Cloud deployment and API integration.

## Author
**Harshitha Evani**