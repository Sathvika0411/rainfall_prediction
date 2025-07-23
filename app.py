import pandas as pd
import pickle  # or use pickle
import numpy as np

# Load the trained model
model = pickle.load('rainfall_model.pkl')

# Create a sample input dictionary
sample_input = {
    'pressure': [1013],
    'dewpoint': [20],
    'humidity': [85],
    'cloud': [7],
    'sunshine': [3],
    'winddirection': [120],
    'windspeed': [15]
}

# Convert to DataFrame
input_df = pd.DataFrame(sample_input)

# Make prediction
prediction = model.predict(input_df)

print(f"Predicted Rainfall: {prediction[0]}")
