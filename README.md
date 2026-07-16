# IoT Network Intrusion Detection System

## Overview

This project is a Machine Learning based IoT Network Intrusion Detection System that classifies network traffic into multiple attack categories using a Random Forest classifier with Boruta Feature Selection.

## Features

- Multi-class intrusion detection
- Boruta feature selection
- Random Forest classifier
- Streamlit web interface
- Manual feature input
- Confidence score prediction

## Attack Classes

- DoS
- MITM ARP Spoofing
- Mirai
- Normal
- Scan

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Project Structure

```
IoT-Network-Intrusion-Detection
│
├── app.py
├── best_model.pkl
├── label_encoder.pkl
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Model

- Algorithm: Random Forest
- Feature Selection: Boruta
- Number of Selected Features: 15
- Classification: Multi-Class

## Author

Harshitha Evani