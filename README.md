markdown

# Iris Flower Species Prediction Project

## Overview

This project is a web application that predicts the species of an iris flower based on its sepal and petal measurements using a K-Nearest Neighbors (KNN) machine learning model. The application is built with Flask and provides a simple interface for users to input flower measurements and receive predictions.

## Features

- **Machine Learning Model**: Uses a KNN classifier trained on the classic Iris dataset
- **Web Interface**: Simple HTML form for user input
- **Real-time Predictions**: Returns species predictions instantly
- **Data Scaling**: Includes standardization of input features using StandardScaler

## Project Structure

iris-flower-prediction/
│
├── app_iris.py # Flask application script
├── IRIS USING KNN.py # Model training script
├── Iris.csv # Dataset
├── KNN.pkl # Serialized KNN model
├── scaler.pkl # Serialized StandardScaler
├── index.html # Web interface template
└── README.md # Project documentation
text


## Requirements

- Python 3.x
- Flask
- scikit-learn
- numpy
- pandas
- pickle

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-flower-prediction.git
   cd iris-flower-prediction

    Install the required packages:
    bash

    pip install flask scikit-learn numpy pandas

Usage

    Run the Flask application:
    bash

python app_iris.py

Open a web browser and navigate to:
text

    http://localhost:5000

    Enter the iris flower measurements in the form and click "Predict" to see the species prediction.

Model Training

The KNN model was trained with the following specifications:

    Test size: 20% of the dataset

    Random state: 0 for reproducibility

    StandardScaler used for feature scaling

    Default KNN parameters (n_neighbors=5)

The model achieved an accuracy score of 96.67% on the test set.
File Descriptions

    app_iris.py: Main Flask application that handles web requests and predictions

    IRIS USING KNN.py: Script for training and saving the KNN model

    Iris.csv: Dataset containing iris flower measurements

    KNN.pkl: Serialized KNN model

    scaler.pkl: Serialized StandardScaler for feature scaling

    index.html: HTML template for the web interface

Future Improvements

    Add data validation for user inputs

    Visualize prediction results with charts

    Implement model versioning

    Add more detailed error handling

    Create a more sophisticated UI

License

This project is open source and available under the MIT License.
Acknowledgments

    The Iris dataset, a classic dataset in machine learning and statistics

    scikit-learn for providing the machine learning algorithms

    Flask for the web framework
