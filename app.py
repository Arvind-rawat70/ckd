import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load("ckd_model.pkl")

# -----------------------------
# App UI
# -----------------------------
st.title("🩺 Chronic Kidney Disease Prediction App")
st.write("Enter patient values below to predict CKD")

# -----------------------------
# Input Fields
# -----------------------------
sc = st.number_input("Serum Creatinine (sc)", min_value=0.0, max_value=20.0)
bu = st.number_input("Blood Urea (bu)", min_value=0.0, max_value=200.0)
al = st.number_input("Albumin (al)", min_value=0.0, max_value=5.0)
hemo = st.number_input("Hemoglobin (hemo)", min_value=0.0, max_value=20.0)
sg = st.number_input("Specific Gravity (sg)", min_value=1.000, max_value=1.030)
bgr = st.number_input("Blood Glucose Random (bgr)", min_value=0.0, max_value=500.0)
pcv = st.number_input("Packed Cell Volume (pcv)", min_value=0.0, max_value=60.0)
pot = st.number_input("Potassium (pot)", min_value=0.0, max_value=10.0)

# Categorical Features (0/1)
dm = st.selectbox("Diabetes Mellitus (dm)", [0, 1])
htn = st.selectbox("Hypertension (htn)", [0, 1])
pe = st.selectbox("Pedal Edema (pe)", [0, 1])

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict CKD"):

    # -----------------------------
    # Create Input DataFrame
    # -----------------------------
    input_data = pd.DataFrame([{
        "sc": float(sc),
        "bu": float(bu),
        "al": float(al),
        "hemo": float(hemo),
        "sg": float(sg),
        "bgr": float(bgr),
        "pcv": float(pcv),
        "pot": float(pot),
        "dm": int(dm),
        "htn": int(htn),
        "pe": int(pe)
    }])

    # -----------------------------
    # Debug Info (optional)
    # -----------------------------
    st.write("📌 Input Data Sent to Model:")
    st.dataframe(input_data)

    # -----------------------------
    # Predict
    # -----------------------------
    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ Patient has Chronic Kidney Disease (CKD)")
        else:
            st.success("✅ Patient does NOT have CKD")

    except Exception as e:
        st.error("❌ Prediction Failed بسبب model pipeline mismatch")
        st.write("Error Details:", e)
