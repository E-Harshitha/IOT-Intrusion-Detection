import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("xgb_model.pkl")
le = joblib.load("label_encoder.pkl")
selected_features = joblib.load("selected_features.pkl")

st.title("Cyber Attack Classification")

st.write("Enter feature values to predict the attack type.")

user_input = {}

for feature in selected_features:
    user_input[feature] = st.number_input(feature, value=0.0)

if st.button("Predict"):

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)

    attack_name = le.inverse_transform(prediction)

    st.success(f"Predicted Attack: {attack_name[0]}")
