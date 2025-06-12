import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Aamir Bin Raheem\RESUME PROJECTS/IRIS MODEL KNN\iris.csv")

X = df.iloc[:, 1:5].values
y = df.iloc[:, 5].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()
KNN.fit(X_train, y_train)

y_pred = KNN.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac) 

variance = KNN.score(X_test, y_test) # checking the score of test
print(variance)

bias = KNN.score(X_train, y_train) # checking the score of train
print(bias)

import pickle

#save the file name
filename = 'KNN.pkl'

#open the file and dump the model
with open(filename, 'wb') as file:
    pickle.dump(KNN, file)

# Save the scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(sc, f)

print("Model has been pickled and saved as KNN.pkl")
