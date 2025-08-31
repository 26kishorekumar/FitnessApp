from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to ACEest_Fitness and Gym! The server is running."})

def calculate_bmi(weight_kg, height_m):
    if not all(isinstance(arg, (int, float)) for arg in [weight_kg, height_m]) or height_m <= 0:
        raise ValueError("Invalid input for BMI calculation.")
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)