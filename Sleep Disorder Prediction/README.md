# 💤 Sleep Disorder Prediction Web App

This project is a machine learning-powered **Flask web application** that predicts whether an individual has a **sleep disorder** — such as **Insomnia**, **Sleep Apnea**, or **None** — based on various health and lifestyle features.

---

## 🚀 Demo

A simple web form allows users to enter their details such as age, gender, stress levels, sleep duration, etc. Once submitted, the model processes the input and displays the predicted sleep disorder category.

[![Sleep Disorder App Screenshot](sleep-disorder-app.png)](https://github.com/Aamir-Raheem/python_programming/blob/main/Sleep%20Disorder%20Prediction/sleep-disorder-app.png)


---

## 🧠 Model Overview

- **Algorithm Used**: LightGBM Classifier (`LGBMClassifier`)
- **Accuracy Achieved**: 91%
- **Target Labels**:
  - 0: Insomnia
  - 1: None
  - 2: Sleep Apnea

The model was trained using a health and lifestyle dataset that includes biometric data, daily habits, and self-reported stress/sleep quality scores.

---

## 📊 Features Used

- Gender (0 = Female, 1 = Male)
- Age
- Occupation (numerically encoded)
- Sleep Duration (in hours)
- Quality of Sleep (1–10)
- Physical Activity Level (0–10)
- Stress Level (1–10)
- BMI Category (numerically encoded)
- Heart Rate
- Daily Steps
- Systolic Blood Pressure
- Diastolic Blood Pressure

---

## 🏗️ Project Structure

```
Sleep-Disorder-Prediction/
│
├── app/
│   ├── LGBM_app.py          # Flask web application
│   ├── index.html           # Frontend HTML form
│   └── LGBM.pkl             # Trained LightGBM model
│
├── model_building/
│   └── HEALTH_PROJECT.py    # Model training and preprocessing script
│
├── data/
│   └── Sleep_health_and_lifestyle_dataset.csv
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore
```

---

## ⚙️ How to Run Locally

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Sleep-Disorder-Prediction.git
cd Sleep-Disorder-Prediction
```

### 📦 2. Install Dependencies

Make sure Python is installed (3.7+), then:

```bash
pip install -r requirements.txt
```

### 🚀 3. Launch the App

```bash
python app/LGBM_app.py
```

### 🌐 4. Open in Browser

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Dataset Source

The dataset used is named:
**`Sleep_health_and_lifestyle_dataset.csv`**
It contains anonymized health and lifestyle attributes of individuals, along with labeled sleep disorder outcomes.

---

## ✍️ Author

**Aamir Bin Raheem**
📧 [aamirraheem6@gmail.com](mailto:aamirraheem6@gmail.com)
📍 Hyderabad, India
💼 [LinkedIn](#) *(Add your profile URL)*

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🙌 Acknowledgments

- LightGBM by Microsoft
- Flask for lightweight web hosting
- [Kaggle](https://www.kaggle.com/) (if dataset is from there)
- Scikit-learn for preprocessing and metrics

---
