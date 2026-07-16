import streamlit as st
import pandas as pd
import joblib

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="IoT Network Intrusion Detection",
    page_icon="🛡️",
    layout="centered"
)

# -----------------------
# Load Model
# -----------------------
model = joblib.load("best_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("🛡️ IoT Network Intrusion Detection")
st.markdown("### Multi-Class Attack Prediction")

st.write("Enter the network traffic details below.")

st.divider()

# -----------------------
# Input Fields
# -----------------------

src_port = st.number_input("Source Port", value=443)

dst_port = st.number_input("Destination Port", value=80)

protocol = st.number_input("Protocol", value=6)

flow_duration = st.number_input("Flow Duration", value=1000.0)

totlen_bwd_pkts = st.number_input("Total Length Backward Packets", value=0.0)

totlen_fwd_pkts = st.number_input("Total Length Forward Packets", value=0.0)

fwd_pkt_len_min = st.number_input("Forward Packet Length Min", value=0.0)

fwd_pkt_len_max = st.number_input("Forward Packet Length Max", value=0.0)

bwd_pkt_len_mean = st.number_input("Backward Packet Length Mean", value=0.0)

bwd_pkt_len_min = st.number_input("Backward Packet Length Min", value=0.0)

fwd_pkt_len_mean = st.number_input("Forward Packet Length Mean", value=0.0)

bwd_pkt_len_max = st.number_input("Backward Packet Length Max", value=0.0)

flow_iat_std = st.number_input("Flow IAT Std", value=0.0)

flow_iat_mean = st.number_input("Flow IAT Mean", value=0.0)

flow_pkts = st.number_input("Flow Packets/sec", value=0.0)

st.divider()

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Attack", use_container_width=True):

    sample = pd.DataFrame([[
        src_port,
        dst_port,
        protocol,
        flow_duration,
        totlen_bwd_pkts,
        totlen_fwd_pkts,
        fwd_pkt_len_min,
        fwd_pkt_len_max,
        bwd_pkt_len_mean,
        bwd_pkt_len_min,
        fwd_pkt_len_mean,
        bwd_pkt_len_max,
        flow_iat_std,
        flow_iat_mean,
        flow_pkts
    ]],
    columns=[
        "Src_Port",
        "Dst_Port",
        "Protocol",
        "Flow_Duration",
        "TotLen_Bwd_Pkts",
        "TotLen_Fwd_Pkts",
        "Fwd_Pkt_Len_Min",
        "Fwd_Pkt_Len_Max",
        "Bwd_Pkt_Len_Mean",
        "Bwd_Pkt_Len_Min",
        "Fwd_Pkt_Len_Mean",
        "Bwd_Pkt_Len_Max",
        "Flow_IAT_Std",
        "Flow_IAT_Mean",
        "Flow_Pkts/s"
    ])

    prediction = model.predict(sample)

    attack = label_encoder.inverse_transform(prediction)[0]

    probability = model.predict_proba(sample).max() * 100

    st.success(f"### Predicted Attack : {attack}")

    st.info(f"Confidence : {probability:.2f}%")

st.divider()

st.caption("Developed using Random Forest and Boruta Feature Selection")