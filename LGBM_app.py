from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('LGBM.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Helper functions to safely convert input
        def get_int(name):
            val = request.form.get(name, '').strip()
            if val == '':
                raise ValueError(f"'{name}' field is required and must be a number.")
            return int(val)

        def get_float(name):
            val = request.form.get(name, '').strip()
            if val == '':
                raise ValueError(f"'{name}' field is required and must be a number.")
            return float(val)

        # Get and validate all inputs
        gender = get_int('gender')  # 0 = Female, 1 = Male
        age = get_int('age')
        occupation = get_int('occupation')  # must match label encoding
        sleep_duration = get_float('sleep_duration')
        quality_of_sleep = get_int('quality_of_sleep')
        physical_activity = get_int('physical_activity')
        stress_level = get_int('stress_level')
        bmi_category = get_int('bmi_category')  # must match label encoding
        heart_rate = get_int('heart_rate')
        daily_steps = get_int('daily_steps')
        systolic = get_int('systolic')
        diastolic = get_int('diastolic')

        # Format input for model
        input_data = np.array([[gender, age, occupation, sleep_duration,
                                quality_of_sleep, physical_activity, stress_level,
                                bmi_category, heart_rate, daily_steps,
                                systolic, diastolic]])
        
        # Predict
        prediction = model.predict(input_data)[0]

        # Map prediction back to label
        result = ["Insomnia", "None", "Sleep Apnea"][prediction]  # Ensure this matches LabelEncoder

        return render_template('index.html', prediction_text=f'Sleep Disorder Prediction: {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)


