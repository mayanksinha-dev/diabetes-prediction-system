from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    values = [
        float(request.form["pregnancies"]),
        float(request.form["glucose"]),
        float(request.form["bloodpressure"]),
        float(request.form["skinthickness"]),
        float(request.form["insulin"]),
        float(request.form["bmi"]),
        float(request.form["dpf"]),
        float(request.form["age"])
    ]

    data = np.array([values])

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)[0]

    result = "Diabetic" if prediction == 1 else "Non-Diabetic"

    return render_template(
        "result.html",
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)