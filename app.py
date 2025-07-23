import streamlit as st
import pickle
import numpy as np

# Load the model
with open('rainfall_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Rainfall Prediction App")

# Input fields
temperature = st.number_input("Enter Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
humidity = st.number_input("Enter Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Rainfall"):
    features = np.array([[temperature, humidity]])
    prediction = model.predict(features)
    st.success(f"Predicted Rainfall: {prediction[0]:.2f} mm")
