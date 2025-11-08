Machine Learning Regression Project with Flask Web App
<p align="center"> <img src="https://img.shields.io/badge/Machine%20Learning-Project-blue" /> <img src="https://img.shields.io/badge/Flask-Backend-black" /> <img src="https://img.shields.io/badge/Scikit--Learn-Model-green" /> <img src="https://img.shields.io/badge/Python-3.10+-yellow" /> <img src="https://img.shields.io/badge/Status-Active-success" /> </p>

A complete end-to-end machine learning project that predicts the selling price of a used car using key input parameters like model name, company, year, kilometers driven, and fuel type.
This repository contains the ML model, training notebook, Flask backend, and a simple responsive frontend.

car-price-predictor/
│── model/
│   └── model.pkl
│── static/
│   └── style.css
│── templates/
│   └── index.html
│── app.py
│── dataset.csv
│── notebook.ipynb
│── requirements.txt
└── README.md

## Clone Repo
git clone https://github.com/DeepTensor-3070/Car-Price-Predictor.git
cd car-price-predictor

## Install dependencies
pip install -r requirements.txt

## Run Flask Server
python app.py

## Visit the App
http://127.0.0.1:5000/

## Sample Request
{
  "name": "Swift",
  "company": "Maruti",
  "year": 2019,
  "kms_driven": 30000,
  "fuel_type": "Petrol"
}

## Sample Response
{
  "prediction": 520000
}

## 👤 Author
Subhanshu Verma
Data Scientist

