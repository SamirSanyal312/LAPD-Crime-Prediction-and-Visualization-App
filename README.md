# Group_4
# LAPD Crime Prediction and Visualization App

This project leverages machine learning to predict crime types using LAPD crime data and visualizes crime hotspots using interactive maps. It features a Random Forest Classifier hosted as a Flask API, with an interactive frontend for user input and a dynamic heatmap for visualization.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoint](#api-endpoint)
6. [Visualization](#visualization)
7. [File Structure](#file-structure)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## Overview

- **Prediction Model**: A Random Forest Classifier trained on LAPD crime data.
- **Frontend**: A user-friendly interface built with HTML, CSS, and JavaScript.
- **Visualization**: Heatmap showing crime hotspots using `folium`.
- **Deployment**: Local Flask server.

---

## Features

1. **Machine Learning Prediction**:
   - Predict crime categories using 20 input features.
   - Trained with optimized preprocessing and feature selection.

2. **API Integration**:
   - Hosted via a Flask backend API.
   - Easily testable with JSON input and output.

3. **Frontend**:
   - Interactive user interface for entering feature values.
   - Displays predictions and probabilities.

4. **Heatmap Visualization**:
   - Generates crime heatmaps using `folium`.
   - Visualizes crime-prone areas using location data.

---

## Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/lapd-crime-prediction.git
cd lapd-crime-prediction

### 2. Install Dependencies:
Install the necessary Python libraries:

bash
Copy code
pip install -r requirements.txt

### 3. Run the Application:
Start the Flask server using:

bash
Copy code
python app.py
Open the application in your browser: http://127.0.0.1:5000

Usage
Frontend:

Navigate to http://127.0.0.1:5000/frontend.
Input 20 feature values as comma-separated values.
Click Predict to get results.
API Endpoint:

Route: /predict
Method: POST
Input Format:
json
Copy code
{
  "data": [0.5, 1.2, 3.4, ..., 4.4]
}
Output Format:
json
Copy code
{
  "prediction": 354,
  "probabilities": [0.1, 0.2, 0.3, ..., 0.05]
}


File Structure
graphql
Copy code
lapd-crime-prediction/
│-- app.py                 # Flask app to host the API and frontend
│-- random_forest_model.pkl # Trained Random Forest model
│-- requirements.txt       # List of Python dependencies
│-- templates/
│   └── index.html         # Frontend HTML file
│-- crime_heatmap.html     # Generated interactive heatmap
│-- README.md              # Project documentation


### Future Enhancements
Deploy the application to a cloud platform (e.g., AWS, Heroku).
Integrate real-time crime data APIs for live predictions.
Add advanced machine learning models (e.g., XGBoost, LSTM).
License
This project is licensed under the MIT License.

Author
Samir Sanyal
sasanyal@iu.edu
https://github.com/SamirSanyal312

Rajat Sawant
rsawant@iu.edu
https://github.iu.edu/rsawant

---

### **requirements.md**

```markdown
# Requirements

The following libraries and tools are required to run the LAPD Crime Prediction App.

## Python Version:
- Python 3.8 or higher

## Python Libraries:
1. **Flask**: For backend server and API hosting.
2. **Pandas**: For data manipulation and preprocessing.
3. **NumPy**: For numerical operations.
4. **Scikit-learn**: For machine learning model training.
5. **Folium**: For generating heatmaps and maps.
6. **Matplotlib**: For visualization purposes.
7. **Seaborn**: For visualizing feature relationships.
8. **Gunicorn**: For production-ready server deployment.

## Development Tools:
- Code Editor (e.g., VSCode, PyCharm)
- Browser (e.g., Chrome, Firefox)
- Command Line Interface (CLI) or Terminal
