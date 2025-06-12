# Iris Flower Species Prediction using K-Nearest Neighbors (KNN)

This project demonstrates a simple web application that predicts the species of an Iris flower based on its sepal length, sepal width, petal length, and petal width. The prediction model is built using the K-Nearest Neighbors (KNN) algorithm and deployed using Flask.

## Project Structure

The repository contains the following key files:

* `IRIS USING KNN.py`: This script is used to train the K-Nearest Neighbors (KNN) model on the Iris dataset, evaluate its performance, and save the trained model using `pickle`.
* `KNN.pkl`: This is the pickled (serialized) machine learning model (K-Nearest Neighbors classifier) trained in `IRIS USING KNN.py`. It's used by the Flask application for making predictions.
* `Iris.csv`: The dataset containing the Iris flower measurements and their corresponding species.
* `app_iris.py`: This is the Flask web application script. It loads the trained KNN model and serves an HTML page for users to input measurements and get predictions.
* `index.html`: The HTML template for the web interface, providing a form for user input and displaying the prediction results.
* `scaler.pkl` (Optional, but recommended): If you used `StandardScaler` during model training (which is good practice for KNN), this file would contain the fitted scaler. The `app_iris.py` code includes a `try-except` block to load it, so it's good to include it if you used one. If you haven't saved it yet, you should add the following line to `IRIS USING KNN.py` after `sc = StandardScaler()` and before `import pickle`:
    ```python
    pickle.dump(sc, open('scaler.pkl', 'wb'))
    ```

## Features

* **Machine Learning Model:** Utilizes the K-Nearest Neighbors (KNN) algorithm for classification.
* **Data Preprocessing:** Includes data splitting into training and testing sets, and feature scaling using `StandardScaler`.
* **Model Evaluation:** Calculates accuracy and displays a confusion matrix.
* **Web Interface:** A simple web form built with Flask allows users to input Iris measurements.
* **Real-time Prediction:** Provides instant predictions of Iris species based on user input.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

Make sure you have Python installed. This project uses several Python libraries which can be installed via `pip`.

```bash
pip install numpy pandas scikit-learn matplotlib flask

Installation and Setup

    Clone the repository:
    Bash

git clone [https://github.com/Aamir-Raheem/Iris-Flower-Prediction.git](https://github.com/Aamir-Raheem/Iris-Flower-Prediction.git)
cd Iris-Flower-Prediction

Train and Save the Model (if KNN.pkl or scaler.pkl are missing or outdated):
First, ensure you have the Iris.csv file in the correct location (as referenced in IRIS USING KNN.py).
Run the IRIS USING KNN.py script to train the model and save it as KNN.pkl and scaler.pkl (if applicable).
Bash

python "IRIS USING KNN.py"

Run the Flask Application:
Ensure you have KNN.pkl, scaler.pkl (if used), and index.html in the same directory as app_iris.py.
Then, run the Flask application:
Bash

    python app_iris.py

    Access the Web Application:
    Open your web browser and navigate to the address provided in your terminal (usually http://127.0.0.1:5000/).

How to Use

    On the web page, you will see input fields for:
        Sepal Length
        Sepal Width
        Petal Length
        Petal Width
    Enter the numerical measurements for an Iris flower.
    Click the "Predict" button.
    The predicted Iris species will be displayed below the form.

Model Details

    Algorithm: K-Nearest Neighbors (KNN)
    Dataset: Iris dataset (Iris.csv)
    Training Split: 80% training, 20% testing
    Preprocessing: StandardScaler is used to scale features.

Contributing

Feel free to fork this repository, make improvements, and submit pull requests.
License

This project is open source and available under the MIT License.
Contact

Aamir Bin Raheem - aamirraheem66@gmail.com
