# 💼 Salary Prediction using Simple Linear Regression

This project uses **Simple Linear Regression** to predict an individual's salary based on their **years of experience**. It includes model training, evaluation, and a user-friendly web application built using **Streamlit**.

---

## 📊 Dataset

The dataset contains 30 records of employees with the following columns:

- `YearsExperience`: Number of years of professional experience.
- `Salary`: Annual salary (in USD).

### Sample Data

| YearsExperience | Salary  |
|-----------------|---------|
| 1.1             | 39343   |
| 5.3             | 83088   |
| 10.5            | 121872  |

---

## 🔍 Project Structure

- `Salary_Data.csv` – Dataset used for training.
- `SLR.pkl` – Pickled model file trained using scikit-learn.
- `salary_predictor_app.py` – Streamlit app to interact with the model.
- `model_training_script.py` – Python script used for training and analysis.

---

## 📈 Model Evaluation Metrics

| Metric | Value |
|--------|-------|
| SSR (Sum of Squares due to Regression) | 6,263,152,884.28 |
| SSE (Sum of Squared Errors)            | 15,274,062,883.94 |
| SST (Total Sum of Squares)             | 108,429,703,765.83 |
| R² Score                                | 0.9422 |

> ✅ The R² value of **0.94** indicates that the model explains **94% of the variance** in salary based on experience — a very good fit for a simple linear model.

---

## 🚀 How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/Aamir-Raheem/salary-prediction-app.git
   cd salary-prediction-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the Streamlit app:
   ```bash
   streamlit run salary_predictor_app.py
   ```

---

## 🧠 Tech Stack

- Python
- Pandas, NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Pickle

---

## 📸 App Screenshot

![App Screenshot](https://github.com/Aamir-Raheem/python_programming/blob/main/Salary%20Prediction/Salary%20App%20SS.png)

---

## 🔗 Connect with Me

- 📍 GitHub: [Aamir-Raheem](https://github.com/Aamir-Raheem)
- 💼 LinkedIn: [Aamir Raheem](https://www.linkedin.com/in/aamir-raheem-a8b3541b3/)

---

## 📌 Author

**Aamir Bin Raheem**
