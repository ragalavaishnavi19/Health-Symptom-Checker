import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def predict_disease(symptoms):

    # Load dataset
    data = pd.read_csv("dataset.csv")

    # Features
    X = data[
        ["Fever", "Cough", "Headache",
         "Fatigue", "BodyPain", "SoreThroat"]
    ]

    # Target
    y = data["Disease"]

    # Create Decision Tree model
    model = DecisionTreeClassifier(random_state=42)

    # Train model
    model.fit(X, y)

    # Predict disease
    disease = model.predict([symptoms])[0]

    # Dummy confidence score
    confidence = 95

    return disease, confidence