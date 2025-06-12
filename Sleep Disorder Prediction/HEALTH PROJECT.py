import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load data
df = pd.read_csv(r"C:\Users\Aamir Bin Raheem\HEALTH PROJECT\Sleep_health_and_lifestyle_dataset.csv", na_values=[],keep_default_na=False)

# Split blood pressure
df[['Systolic', 'Diastolic']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)
df.drop('Blood Pressure', axis=1, inplace=True)

# Encode categorical features
categorical_cols = ['Gender', 'Occupation', 'BMI Category']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
df['Sleep Disorder'] = target_encoder.fit_transform(df['Sleep Disorder'])

# Define features and target (after all preprocessing)
X = df.drop(columns=['Person ID', 'Sleep Disorder']).values
y = df['Sleep Disorder'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Model training
LGBM = LGBMClassifier()
LGBM.fit(X_train, y_train)

# Prediction
y_pred = LGBM.predict(X_test)

# Accuracy
ac = accuracy_score(y_test, y_pred)
print(f"Accuracy: {ac:.2f}")

# Save model
with open('LGBM.pkl', 'wb') as file:
    pickle.dump(LGBM, file)
