import pickle
from flask import Flask, request, jsonify, render_template

# Load the trained Random Forest model
try:
    with open('random_forest_model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Model file 'random_forest_model.pkl' not found.")
    exit(1)
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Initialize Flask app with a custom template folder
app = Flask(__name__, template_folder="custom_templates")
#app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return (
        "<h1>Welcome to the LAPD Crime Prediction API!</h1>"
        "<p>Use the <code>/predict</code> endpoint for predictions. "
        "Visit <code>/frontend</code> for the user interface.</p>"
    )

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON input
        input_data = request.get_json()

        # Check if input_data exists and contains 'data'
        if not input_data or "data" not in input_data:
            return (
                jsonify(
                    {"error": "Invalid input. Provide 'data' in the request body as a list of 20 features."}
                ),
                400,
            )

        # Extract the data array
        data = input_data["data"]

        # Validate the input length
        expected_features = 20  # Adjust this number based on your model's feature count
        if len(data) != expected_features:
            return (
                jsonify({"error": f"Expected {expected_features} features, but got {len(data)}."}),
                400,
            )

        # Make a prediction
        prediction = model.predict([data])[0]
        probabilities = model.predict_proba([data])[0].tolist()

        # Return the prediction and probabilities
        return jsonify(
            {
                "prediction": int(prediction),
                "probabilities": probabilities,
                "message": "Prediction successful!",
            }
        )
    except KeyError as ke:
        return jsonify({"error": f"Missing key in input: {ke}"}), 400
    except ValueError as ve:
        return jsonify({"error": f"Value error: {ve}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/frontend")
def frontend():
    return render_template("index.html")  # Flask will look for index.html in custom_templates folder

if __name__ == "__main__":
    app.run(debug=True)
