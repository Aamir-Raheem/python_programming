
# 🌸 Iris Species Prediction Using K-Nearest Neighbour

This project is a **Flask web application** powered by a **K-Nearest Neighbour (KNN)** machine learning model to predict the species of an **Iris flower** — such as **Iris-setosa**, **Iris-versicolor**, or **Iris-virginica** — based on floral dimensions.

---

## 🚀 Demo

A simple and intuitive web form allows users to input the flower's measurements. Once submitted, the trained model processes the input and displays the predicted species.

[![Iris App Screenshot](iris.png)](https://github.com/Aamir-Raheem/python_programming/blob/main/Iris%20Prediction%20Using%20KNN/iris.png)

---

## 🧠 Model Overview

- **Algorithm Used**: K-Nearest Neighbour (`KNeighborsClassifier`)
- **Target Labels**:
  - Iris-setosa
  - Iris-versicolor
  - Iris-virginica

The model was trained using the classic Iris dataset containing measurements of sepal and petal lengths and widths.

---

## 📊 Features Used

- Id  
- SepalLengthCm  
- SepalWidthCm  
- PetalLengthCm  
- PetalWidthCm  
- Species *(target)*

---

## 🏗️ Project Structure

```
Iris-Species-Prediction/
│
├── app/
│   ├── app_iris.py               # Flask web application
│   ├── index.html                # Frontend HTML form
│   ├── KNN.pkl                   # Trained KNN model
│   └── scaler.pkl                # Scaler used during preprocessing
│
├── model_building/
│   └── Iris Model Using KNN.py   # Model training and preprocessing script
│
├── data/
│   └── iris.csv                  # Iris dataset
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore
```

---

## ⚙️ How to Run Locally

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Iris-Species-Prediction.git
cd Iris-Species-Prediction
```

### 📦 2. Install Dependencies

Make sure Python is installed (3.7+), then:

```bash
pip install -r requirements.txt
```

### 🚀 3. Launch the App

```bash
python app/app_iris.py
```

### 🌐 4. Open in Browser

Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Dataset Source

The dataset used is:
**`iris.csv`**

It contains floral measurements and species labels for 150 iris flowers, commonly used in ML tutorials and benchmarks.

---

## ✍️ Author

**Aamir Bin Raheem**  
📧 [aamirraheem6@gmail.com](mailto:aamirraheem6@gmail.com)  
📍 Hyderabad, India  
💼 [LinkedIn](https://www.linkedin.com/in/aamir-raheem-a8b3541b3/)

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🙌 Acknowledgments

- UCI Machine Learning Repository for the Iris dataset  
- Scikit-learn for model building  
- Flask for web hosting
