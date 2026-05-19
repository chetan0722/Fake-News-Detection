# Fake-News-Detection
Built a Fake News Detection web application using Python, TF-IDF vectorization, Logistic Regression, and Streamlit. The model classifies news articles as real or fake through a user-friendly interface.
# Fake News Detection using Machine Learning

## Project Overview
This project is a Machine Learning based Fake News Detection system that classifies news articles as **Real** or **Fake**.

The project uses text preprocessing, TF-IDF vectorization, Logistic Regression, and a Streamlit web interface for prediction.

## Features
- News text preprocessing
- TF-IDF feature extraction
- Logistic Regression model
- Real-time prediction
- Streamlit web application

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## Dataset
Dataset files:

- Fake.csv
- True.csv

## Model Workflow
1. Load dataset
2. Clean text data
3. Convert text using TF-IDF
4. Train Logistic Regression model
5. Save model using Pickle
6. Deploy using Streamlit

## Project Structure

```text
Fake-News-Detection
│
├── app.py
├── requirements.txt
├── README.md
└── models
    ├── model.pkl
    └── vectorizer.pkl
