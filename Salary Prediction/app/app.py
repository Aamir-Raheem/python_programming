import streamlit as st
import pickle
import numpy as np
import os

# App title and subtitle
st.set_page_config(page_title="Salary Prediction", layout="centered")
st.title("💼 Salary Prediction App")
st.markdown("Predict your salary based on your **years of experience** using a trained Simple Linear Regression model.")

# Load the saved model with error handling
model_path = r'C:\Users\Aamir Bin Raheem\RESUME PROJECTS\Salary Prediction\SLR.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
else:
    st.error("Model file not found. Please ensure 'SLR.pkl' is in the correct location.")
    st.stop()

# Input: Years of Experience
years_experience = st.number_input(
    "🔢 Enter Years of Experience:",
    min_value=0.0, max_value=50.0,
    value=1.0, step=0.5
)

# Prediction logic
if st.button("🎯 Predict Salary"):
    # Prepare input and make prediction
    experience_input = np.array([[years_experience]])  # 2D array required for prediction
    prediction = model.predict(experience_input)
    
    # Display prediction
    st.success(f"💰 Estimated Salary for {years_experience} years of experience: **${prediction[0]:,.2f}**")

# Footer / Model Info
st.markdown("---")
st.markdown("📌 *This model was built and trained by **Aamir Bin Raheem** using a dataset of salaries and years of experience.*")
