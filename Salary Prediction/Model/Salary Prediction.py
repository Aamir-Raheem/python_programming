# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Aamir Bin Raheem\RESUME PROJECTS\Salary Prediction\Salary_Data.csv")

# Separate features and target variable
x = df.iloc[:, :-1]  # Independent variable (Years of Experience)
y = df.iloc[:, -1]   # Dependent variable (Salary)

# Split data into training and test sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# Train the Linear Regression model
from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Predict salaries for test set
y_pred = regressor.predict(x_test)

# Visualize the test set results
plt.scatter(x_test, y_test, color='red')  # Actual salaries
plt.plot(x_train, regressor.predict(x_train), color='blue')  # Regression line
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Get the slope (coefficient)
m_slope = regressor.coef_
print(m_slope)

# Get the intercept
c_intercept = regressor.intercept_
print(c_intercept)

# Predict salary for a 12-year-experienced employee
pred_12yr_emp_ecp = m_slope * 12 + c_intercept
print(pred_12yr_emp_ecp)

# Get R^2 score for training data (bias)
bias = regressor.score(x_train, y_train)

# Get R^2 score for test data (variance)
variance = regressor.score(x_test, y_test)
print(variance)

'''----------------------STATS FOR ML-------------------------'''

# Mean of all columns
df.mean()

# Mean of Salary column
df["Salary"].mean()

# Median of all columns
df.median()

# Median of Salary column
df["Salary"].median()

# Mode of Salary column
df['Salary'].mode()

# Variance of all columns
df.var()

# Variance of Salary column
df['Salary'].var()

# Standard deviation of all columns
df.std()

# Standard deviation of Salary column (repeat of var call — likely a typo)
df["Salary"].var()

# Coefficient of variation (relative std dev)
from scipy.stats import variation
variation(df.values)

# Coefficient of variation of Salary column
variation(df['Salary'])

# Correlation matrix
df.corr()

'''-----------------MANUAL CALCULATION OF REGRESSION METRICS------------------'''

# Total sum of squares due to regression (SSR)
y_mean = np.mean(y)
SSR = np.sum((y_pred - y_mean) ** 2)
print("SSR:", SSR)

# Sum of squared errors (SSE)
y = y[0:6]  # To match y_pred size
SSE = np.sum((y - y_pred) ** 2)
print("SSE:", SSE)

# Total sum of squares (SST)
mean_total = np.mean(df.values)
SST = np.sum((df.values - mean_total) ** 2)
print("SST:", SST)

# R-squared calculation
r_square = 1 - SSR/SST
print("r_square:", r_square)

'''----------------------SAVE MODEL USING PICKLE-------------------------'''

import pickle

# Save the model to disk
filename = 'SLR.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
    
print("Model has been pickled and saved as SLR.pkl")

# Check current working directory
import os
os.getcwd()

