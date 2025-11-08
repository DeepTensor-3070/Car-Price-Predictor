from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("model.pkl")

# Load original CSV to populate dropdowns
df = pd.read_csv("Cleaned_Data.csv")

car_names = sorted(df["name"].unique())
companies = sorted(df["company"].unique())
fuel_types = sorted(df["fuel_type"].unique())

@app.route("/")
def home():
    return render_template(
        "index.html",
        car_names=car_names,
        companies=companies,
        fuel_types=fuel_types
    )

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_df = pd.DataFrame([{
        "name": data["car_name"],
        "company": data["car_type"],
        "year": int(data["year"]),
        "kms_driven": float(data["kms"]),
        "fuel_type": data["fuel_type"]
    }])

    predicted_price = model.predict(input_df)[0]

    return jsonify({
        "price": round(float(predicted_price), 2),
        "market_low": round(float(predicted_price) * 0.90, 2),
        "market_avg": round(float(predicted_price) * 0.95, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
