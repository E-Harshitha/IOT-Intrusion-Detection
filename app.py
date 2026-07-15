import streamlit as st
import pandas as pd
import joblib
import os
import gdown

# Download model if not present
MODEL_ID = "1FsiJAG3W_UzV4fzutHv9hjwFtfwSr8jd"

if not os.path.exists("best_model.pkl"):
    gdown.download(
        f"https://drive.google.com/uc?id={MODEL_ID}",
        "best_model.pkl",
        quiet=False
    )

model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="IoT Network Intrusion Detection",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ IoT Network Intrusion Detection")

st.write("Enter the network traffic details.")

dst_port = st.number_input("Destination Port", value=80)

init_bwd_win = st.number_input("Initial Backward Window Bytes", value=0)

src_port = st.number_input("Source Port", value=443)

flow_duration = st.number_input("Flow Duration", value=1000.0)

ack_flag = st.number_input("ACK Flag Count", value=1)

bwd_header = st.number_input("Backward Header Length", value=0)

if st.button("Predict"):

    data = pd.DataFrame([[
        dst_port,
        init_bwd_win,
        src_port,
        flow_duration,
        ack_flag,
        bwd_header
    ]], columns=[
        "Dst_Port",
        "Init_Bwd_Win_Byts",
        "Src_Port",
        "Flow_Duration",
        "ACK_Flag_Cnt",
        "Bwd_Header_Len"
    ])

    data = scaler.transform(data)

    prediction = model.predict(data)

    result = label_encoder.inverse_transform(prediction)[0]

    if result == "Anomaly":
        st.error("⚠️ Intrusion Detected (Anomaly)")
    else:
        st.success("✅ Normal Network Traffic")
