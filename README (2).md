# Cyber Attack Classification Using XGBoost

## 📌 Project Overview

This project is a Machine Learning-based Cyber Attack Classification system developed using the **XGBoost** algorithm. The model classifies different types of cyber attacks based on network traffic features. Mutual Information is used for feature selection, and the trained model is deployed using **Streamlit** for real-time prediction.

---

## 🚀 Features

- Data preprocessing and cleaning
- Mutual Information-based feature selection
- XGBoost classifier for attack prediction
- Label Encoding for target classes
- Model evaluation using Accuracy, Precision, Recall, and F1-Score
- Confusion Matrix visualization
- Streamlit web application for prediction

---

## 📂 Dataset

The dataset contains network traffic records with multiple features and a target column named **Sub_Cat**, representing different cyber attack types.

### Example Attack Classes

- Normal
- DoS-Synflooding
- MITM ARP Spoofing
- Mirai-Ackflooding
- Mirai-HTTP Flooding
- Mirai-UDP Flooding
- Scan Hostport
- Scan Port OS

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

## 📁 Project Structure

```
Cyber-Attack-Classification/
│
├── app.py
├── xgb_model.pkl
├── label_encoder.pkl
├── selected_features.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Cyber-Attack-Classification.git
```

Move into the project directory

```bash
cd Cyber-Attack-Classification
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at

```
http://localhost:8501
```

---

## 📊 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Encode Categorical Features
4. Mutual Information Feature Selection
5. Train-Test Split
6. Train XGBoost Model
7. Evaluate Model Performance
8. Save Trained Model
9. Deploy with Streamlit

---

## 📈 Model Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 💻 Streamlit Application

The Streamlit interface allows users to:

- Enter feature values manually or upload a CSV file.
- Predict the cyber attack category.
- Display the predicted attack type.
- Process multiple records in a single upload.

---

## 📦 Required Libraries

```
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
```

---

## 📸 Application Screenshot

Add screenshots of the Streamlit application here.

```
screenshots/home.png
screenshots/prediction.png
```

---

## 🎯 Future Enhancements

- Support additional machine learning models
- Hyperparameter tuning
- Explainable AI using SHAP values
- Real-time network traffic monitoring
- Cloud deployment

---

## 👩‍💻 Author

**Snehalatha Chandragiri**

---

## 📄 License

This project is developed for educational and research purposes.