import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="IoT Intrusion Detection")

st.title("IoT Network Intrusion Detection")

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    prediction = model.predict(scaler.transform(df))

    prediction = le.inverse_transform(prediction)

    df["Prediction"] = prediction

    st.write(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Results",
        csv,
        "prediction.csv",
        "text/csv"
    )