# 🩺 Diabetes Prediction System

An AI-powered Diabetes Prediction Web Application built using Machine Learning and Flask. The system predicts whether a patient is likely to have diabetes based on medical parameters such as Glucose, BMI, Age, Insulin levels, and other health indicators.

---

## 🚀 Features

* Predict diabetes risk instantly
* User-friendly web interface
* Machine Learning powered predictions
* Real-time form validation
* Responsive design
* Scikit-Learn model integration
* Flask backend deployment

---

## 📊 Model Performance

| Metric                 | Score  |
| ---------------------- | ------ |
| Accuracy               | 74.68% |
| ROC-AUC                | 83.06% |
| Cross Validation Score | 76.05% |

### Most Important Features

* Glucose → 28.25%
* BMI → 17.63%
* Age → 12.90%
* Diabetes Pedigree Function → 10.96%
* Insulin → 9.97%

---

## 🛠 Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask
* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Model Files

* diabetes_model.pkl
* scaler.pkl

---

## 📂 Project Structure

```bash
DiabetesPrediction/
│
├── app.py
├── diabetes_model.pkl
├── scaler.pkl
├── diabetes.csv
├── model_meta.json
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open your browser and visit:

```bash
http://127.0.0.1:5000
```

---

## 🧪 Sample Test Input

| Parameter                | Value |
| ------------------------ | ----- |
| Pregnancies              | 6     |
| Glucose                  | 148   |
| BloodPressure            | 72    |
| SkinThickness            | 35    |
| Insulin                  | 120   |
| BMI                      | 33.6  |
| DiabetesPedigreeFunction | 0.627 |
| Age                      | 50    |

Expected Output:

```text
Diabetic
```

---

## 🔬 Dataset

The model is trained on the PIMA Indians Diabetes Dataset containing medical diagnostic measurements used to predict diabetes occurrence.

Features used:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI
* Diabetes Pedigree Function
* Age

---

## 🎯 Future Enhancements

* Diabetes Risk Percentage
* Interactive Health Dashboard
* BMI Calculator
* Medical Report Upload
* Explainable AI Predictions
* Cloud Deployment
* User Authentication
* Doctor Recommendation System

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Mayank Sinha**

B.Tech CSE (AI & ML)

Machine Learning Enthusiast | Data Analytics | AI Developer

---

⭐ If you found this project useful, don't forget to star the repository.
