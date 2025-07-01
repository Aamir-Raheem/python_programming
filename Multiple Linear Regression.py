# --- Importing Libraries ---
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# --- Load Dataset ---
df = pd.read_csv(r"C:\Users\Aamir Bin Raheem\RESUME PROJECTS\MLR\Investment.csv")

# --- Selecting Variables ---
X = df.iloc[:, :-1]
y = df.iloc[:, 4]

# --- Encoding Categorical Variables ---
X = pd.get_dummies(X, dtype=int)  # keep all columns (drop_first=False)

# --- Splitting into Training and Testing ---
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# --- Train Base Linear Regression (Before Lasso) ---
from sklearn.linear_model import LinearRegression
MLR = LinearRegression()
MLR.fit(X_train, y_train)
y_pred = MLR.predict(X_test)

# --- Metrics Before Lasso ---
from sklearn.metrics import mean_squared_error, r2_score
print("\n--- Linear Regression ---")
print("MSE:", mean_squared_error(y_test, y_pred))
print("SSE:", np.sum((y_test - y_pred) ** 2))
r2 = r2_score(y_test, y_pred)
print("R2:", r2)

# Adjusted R² before Lasso
n = X_test.shape[0]
p = X_test.shape[1]
adjusted_r2 = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)
print("Adjusted R2:", adjusted_r2)

# --- LassoCV for Feature Selection ---
from sklearn.linear_model import LassoCV

lasso = LassoCV(cv=5, alphas=np.logspace(-3, 3, 100), max_iter=10000)
lasso.fit(X_train, y_train)

# --- Evaluate Lasso Model ---
y_pred_lasso = lasso.predict(X_test)
r2_lasso = r2_score(y_test, y_pred_lasso)

# Adjusted R² after Lasso
p_lasso = np.sum(lasso.coef_ != 0)
adjusted_r2_lasso = 1 - ((1 - r2_lasso) * (n - 1)) / (n - p_lasso - 1)

print("\n--- Lasso Regression ---")
print("R2:", r2_lasso)
print("Adjusted R2:", adjusted_r2_lasso)
print("Selected Features Count (p):", p_lasso)
print("Best Alpha:", lasso.alpha_)

# --- Display Selected Feature Names ---
selected_features = X.columns[lasso.coef_ != 0]
print("Selected Features:", selected_features.tolist())

# --- Optional: Retrain Final Model with Selected Features ---
X_selected = X[selected_features]
final_model = LinearRegression()
final_model.fit(X_selected, y)

# Predict on entire data (or split again if needed)
y_final_pred = final_model.predict(X_selected)
r2_final = r2_score(y, y_final_pred)
n_final = X_selected.shape[0]
p_final = X_selected.shape[1]
adjusted_r2_final = 1 - ((1 - r2_final) * (n_final - 1)) / (n_final - p_final - 1)

print("\n--- Final Clean Model ---")
print("Final R2:", r2_final)
print("Final Adjusted R2:", adjusted_r2_final)

import pickle

#save the file name
filename = 'MLR.pkl'

#open the file and dump the model
with open(filename, 'wb') as file:
    pickle.dump(MLR, file)


train_score = MLR.score(X_train, y_train)
test_score = MLR.score(X_test, y_test)

print("Train Score:", train_score)
print("Test Score:", test_score)

# Check for high bias (underfitting)
if train_score < 0.6 and test_score < 0.6:
    print("Model may have High Bias (Underfitting)")

# Check for high variance (overfitting)
elif train_score - test_score > 0.2:
    print("Model may have High Variance (Overfitting)")

# Good fit
else:
    print("Model is likely a Good Fit")
    
'''high train score, low test score ---> overfitting
   low train score, low test score ----> underfitting'''


