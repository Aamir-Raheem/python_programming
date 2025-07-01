import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("MLR.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Profit Prediction App", page_icon="💸", layout="centered")

st.title("💼 Startup Profit Prediction")
st.markdown("Predict your **Profit** based on marketing, promotion, research, and location.")

# Input fields
digital = st.number_input("💻 Digital Marketing Spend", min_value=0.0, step=1000.0, format="%.2f")
promotion = st.number_input("📢 Promotion Spend", min_value=0.0, step=1000.0, format="%.2f")
research = st.number_input("🔬 Research Spend", min_value=0.0, step=1000.0, format="%.2f")
state = st.selectbox("📍 State", ["Bangalore", "Chennai", "Hyderabad"])

# One-hot encode manually
state_bangalore = 1 if state == "Bangalore" else 0
state_chennai = 1 if state == "Chennai" else 0
state_hyderabad = 1 if state == "Hyderabad" else 0  # Can be ignored if only 2 dummies used in training

# Create input DataFrame
input_data = pd.DataFrame({
    "DigitalMarketing": [digital],
    "Promotion": [promotion],
    "Research": [research],
    "State_Bangalore": [state_bangalore],
    "State_Chennai": [state_chennai],
    "State_Hyderabad": [state_hyderabad],  # Include this only if model was trained with 3 dummies
})

# Drop unused dummy if needed (based on your training)
# input_data.drop("State_Hyderabad", axis=1, inplace=True)

# Prediction
if st.button("💰 Predict Profit"):
    profit = model.predict(input_data)[0]
    st.success(f"💸 Estimated Profit: ₹{profit:,.2f}")


