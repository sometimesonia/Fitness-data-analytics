from flask import Flask, render_template
from flask import request
import numpy as np
app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)



@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        # cancer
        if (len(to_predict_list) == 5):
            result = ValuePredictor(to_predict_list, 5)

    if (int(result) == 1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return (render_template("result.html", prediction_text=prediction))


if __name__ == "__main__":
    app.run(debug=True)
