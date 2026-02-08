import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("ckd_model.pkl")

st.title("🩺 Chronic Kidney Disease Prediction App")
st.write("Enter patient values to predict CKD")

# Input fields
sc = st.number_input("Serum Creatinine (sc)", 0.0, 20.0)
bu = st.number_input("Blood Urea (bu)", 0.0, 200.0)
al = st.number_input("Albumin (al)", 0.0, 5.0)
hemo = st.number_input("Hemoglobin (hemo)", 0.0, 20.0)
sg = st.number_input("Specific Gravity (sg)", 1.000, 1.030)
bgr = st.number_input("Blood Glucose Random (bgr)", 0.0, 500.0)
pcv = st.number_input("Packed Cell Volume (pcv)", 0.0, 60.0)
pot = st.number_input("Potassium (pot)", 0.0, 10.0)

dm = st.selectbox("Diabetes Mellitus (dm)", [0, 1])
htn = st.selectbox("Hypertension (htn)", [0, 1])
pe = st.selectbox("Pedal Edema (pe)", [0, 1])

# Predict button
if st.button("Predict CKD"):

    # ✅ Create DataFrame with exact training column names
    input_data = pd.DataFrame([{
        "sc": sc,
        "bu": bu,
        "al": al,
        "hemo": hemo,
        "sg": sg,
        "bgr": bgr,
        "pcv": pcv,
        "pot": pot,
        "dm": dm,
        "htn": htn,
        "pe": pe
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Patient has Chronic Kidney Disease (CKD)")
    else:
        st.success("✅ Patient does NOT have CKD")
