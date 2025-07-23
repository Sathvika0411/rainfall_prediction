import streamlit as st
import pickle
import pandas as pd

# Load the model from pickle
with open('rainfall_model.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data["model"]  # assuming your pkl is a dict with 'model' key

st.title("Rainfall Prediction App")

# Input fields for all 7 features
pressure = st.number_input("Enter Pressure (hPa)", min_value=900.0, max_value=1100.0, step=0.1)
dewpoint = st.number_input("Enter Dew Point (°C)", min_value=-10.0, max_value=40.0, step=0.1)
humidity = st.number_input("Enter Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
cloud = st.number_input("Enter Cloud Cover (%)", min_value=0.0, max_value=100.0, step=1.0)
sunshine = st.number_input("Enter Sunshine (hours)", min_value=0.0, max_value=15.0, step=0.1)
winddirection = st.number_input("Enter Wind Direction (°)", min_value=0.0, max_value=360.0, step=1.0)
windspeed = st.number_input("Enter Wind Speed (km/h)", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Rainfall"):
    # Create input DataFrame
    input_df = pd.DataFrame([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]],
                            columns=['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine',
                                     'winddirection', 'windspeed'])
    
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("🌧️ Rainfall is likely.")
    else:
        st.info("☀️ No rainfall expected.")
