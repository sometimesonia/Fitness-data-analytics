from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('obesity_model.pkl')

@app.route('/')
def home():
    return render_template('obesity.html')

@app.route('/predict_obesity', methods=['POST'])
def predict_obesity():
    if request.method == 'POST':
        # Sample input data provided
        gender = "female"
        age = 20
        height = 157
        weight = 60
        calories = 2500
        activity = "lightly_active"

        # Process inputs for the model
        gender_value = 1 if gender == 'female' else 0
        activity_levels = {'sedentary': 1, 'lightly_active': 2, 'moderately_active': 3, 'very_active': 4}
        activity_value = activity_levels.get(activity, 1)

        # Create the feature array
        features = np.array([[gender_value, age, height, weight, calories, activity_value]])

        # Predict
        prediction = model.predict(features)[0]

        # Generate the prediction text
        prediction_text = "You have a high risk of obesity" if prediction == 1 else "You have a low risk of obesity"

        return render_template('result.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
