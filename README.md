
# 💼 Investment Profit Prediction using Multiple Linear Regression (MLR)

This project predicts **company profit** based on investments in different areas like **Digital Marketing**, **Promotion**, **Research**, and **State** location. The model is trained using **Multiple Linear Regression** and optimized using **LassoCV** for automatic feature selection and performance improvement.

---

## 📁 Dataset

- **Filename:** `Investment.csv`
- **Features:**
  - `DigitalMarketing` — Amount spent on digital marketing
  - `Promotion` — Amount spent on promotions
  - `Research` — Amount spent on R&D
  - `State` — Categorical variable (`Chennai`, `Bangalore`, `Hyderabad`)
- **Target:**
  - `Profit` — Total company profit (in $)

---

## 📊 Model Workflow

1. **Import and explore dataset**
2. **Encode categorical variables** using `pd.get_dummies()`
3. **Split dataset** into training and testing sets (80/20)
4. **Train Linear Regression** model for baseline performance
5. **Use LassoCV** for automatic feature selection and regularization
6. **Retrain model** using only selected features
7. **Evaluate** using metrics:
   - R² (Coefficient of Determination)
   - Adjusted R²
   - MSE and SSE
8. **Export** the final model using `pickle`

---

## 📈 Results

| Stage             | R²           | Adjusted R²     | Selected Features |
|------------------|--------------|------------------|--------------------|
| Base MLR         | ~0.934       | ~0.804           | All                |
| After LassoCV    | ~0.939       | ~0.909           | 3 important ones   |
| Final Clean Model| **0.9507**   | **0.9475**       | Refined features   |

- 📌 **Lasso helped reduce the gap between R² and Adjusted R²** by removing less relevant predictors.

---

## 🧠 Technologies Used

- Python 3
- Pandas, NumPy, Matplotlib
- Scikit-learn
- Statsmodels
- Pickle (for model saving)

---

## 🚀 How to Use

1. Clone the repository or download the files
2. Replace `Investment.csv` with your own dataset (if needed)
3. Run `MLR.py` or Jupyter notebook to train and test
4. The final model is saved as: `MLR.pkl`

---

## 📦 Model Deployment (Optional)

You can use the saved model `MLR.pkl` in a **Streamlit app** or **Flask API** to deploy it as a web service.

---

## 👨‍💻 Author

**Aamir Bin Raheem**  
Data Analyst | Python & ML Enthusiast  
📧 aamirraheem6@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/aamir-raheem-a8b3541b3/)

---

## ⚠️ License

This project is for educational/demo purposes only.
