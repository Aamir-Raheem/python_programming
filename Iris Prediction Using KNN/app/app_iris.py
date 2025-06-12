from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open(r'C:\Users\Aamir Bin Raheem\RESUME PROJECTS/IRIS MODEL KNN\KNN.pkl', 'rb'))


# Load the scaler if you used one
try:
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    scaler = None

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values and convert to float
        features = [float(x) for x in request.form.values()]
        input_array = np.array([features])
        
        # Scale if scaler exists
        if scaler:
            input_array = scaler.transform(input_array)

        # Predict
        prediction = model.predict(input_array)
        result = prediction[0]
        return render_template('index.html', prediction_text=f'Predicted species: {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)
    
