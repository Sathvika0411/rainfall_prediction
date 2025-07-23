from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model (update the path if needed)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features in the correct order as per training
        features = [
            data['pressure'],
            data['maxtemp'],
            data['temparatu'],  # keep key as it is in CSV
            data['mintemp'],
            data['dewpoint'],
            data['humidity'],
            data['cloud'],
            data['rainfall'],
            data['sunshine'],
            data['wind'],
            data['windspeed']
        ]

        # Convert to NumPy array and reshape for prediction
        input_data = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
