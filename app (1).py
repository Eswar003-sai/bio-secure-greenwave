import streamlit as st
import random
import time
import hashlib
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bio-Secure Green-Wave", page_icon="🚨", layout="wide")

st.title("🚨 Bio-Secure Green-Wave: Anti-Abuse Emergency Router")
st.subheader("Smart-City Autonomous Infrastructure Mesh Powered by AI Logic Gates")

# Layout columns for sidebar inputs
st.sidebar.header("🛠️ Simulation Control Dashboard")
ambulance_id = st.sidebar.text_input("Ambulance Vehicle ID", "AMB-7729")
has_patient = st.sidebar.checkbox("Is Patient Physically on Stretcher?", value=True)
hospital_dispatch = st.sidebar.checkbox("Is Hospital Active Dispatch Token Valid?", value=True)

if st.sidebar.button("Execute Live Grid Routing Check"):
    st.write("### 🖥️ Processing Real-Time Telemetry Arrays...")
    
    # 1. Patient Sensor Check Simulation
    patient_verified = 1.0 if has_patient else 0.0
    st.info(f"📊 [Cabin Telemetry Check]: Stretcher Sensor Status = {patient_verified}")
    
    # 2. Cryptographic Token Verification Simulation
    if hospital_dispatch:
        raw_string = f"{ambulance_id}-{time.time()}-CitySmartGridSecret99X"
        token = hashlib.sha256(raw_string.encode()).hexdigest()
        token_verified = 1.0
        st.success(f"🔏 [Hospital Key Verification]: SHA-256 Validated -> `{token[:16]}...`")
        st.success(f"🚨 [POLICE MESH ALERT]: Mobile notification sent to local traffic patrol to clear un-signalized routes!")
    else:
        token_verified = 0.0
        st.warning("⚠️ [Hospital Key Verification]: FORGED, MISMATCHED OR EXPIRED TOKEN ENCOUNTERED!")

    # 3. Validation Logic Gate Execution
    is_legitimate_emergency = (token_verified == 1.0 and patient_verified == 1.0)
    
    # 4. Process Simulation Trajectory
    distance = 400.0
    steps = 0
    distance_history = []
    
    while distance > 0 and steps < 25:
        distance_history.append(distance)
        if is_legitimate_emergency:
            distance -= 30.0  # Priority Green Wave Speed profile
        else:
            distance -= 10.0  # Standard commuter slow delays profile
        steps += 1
    
    # Generate the interactive visualization on the web app interface
    fig, ax = plt.subplots(figsize=(10, 4.5))
    if is_legitimate_emergency:
        ax.plot(distance_history, label="Verified Emergency (Green Wave Corridor Unlocked)", color="#2ecc71", linewidth=3.5, marker="o")
    else:
        ax.plot(distance_history, label="Abuse Flagged / Override Blocked (Standard City Delays)", color="#e74c3c", linewidth=3.5, marker="x")
        
    ax.set_title("Ambulance Travel Velocity Profile to Medical Center", fontsize=12, fontweight="bold")
    ax.set_xlabel("Simulation Elapsed Time Steps (Seconds)")
    ax.set_ylabel("Distance Matrix to Target Destination (Meters)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    st.pyplot(fig)
    
    # Quantitative Results Display box
    st.write("----")
    st.write("#### 📊 Quantitative Simulation Summary Metrics:")
    est_time = steps * 5
    if is_legitimate_emergency:
        st.metric(label="System Priority Authorization State", value="CORRIDOR UNLOCKED", delta=f"{est_time}s Transit Window")
    else:
        st.metric(label="System Priority Authorization State", value="OVERRIDE REJECTED & LOGGED", delta=f"{est_time}s Delayed Transit", delta_color="inverse")
