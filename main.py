from symptom_checker import predict_disease
from report import generate_report
from visualizations import create_visualizations


# Symptoms used by the ML model
symptom_names = [
    "Fever",
    "Cough",
    "Headache",
    "Fatigue",
    "Body Pain",
    "Sore Throat"
]


print("=" * 50)
print("       AI HEALTH SYMPTOM CHECKER")
print("=" * 50)

# Patient details
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")

print("\nEnter 1 for YES and 0 for NO")

symptoms = []

for symptom in symptom_names:

    while True:

        try:
            value = int(input(f"Do you have {symptom}? "))

            if value in [0, 1]:
                symptoms.append(value)
                break

            else:
                print("Please enter only 1 or 0.")

        except ValueError:
            print("Please enter a valid number.")


# Predict disease
disease, confidence = predict_disease(symptoms)


# Display result
print("\n" + "=" * 50)
print("             PREDICTION RESULT")
print("=" * 50)

print("Predicted Disease :", disease)
print("Confidence Score  :", str(confidence) + "%")


# Generate report
generate_report(
    name,
    age,
    gender,
    symptoms,
    symptom_names,
    disease,
    confidence
)


# Create graphs
print("\nCreating visualizations...")

create_visualizations()

print("\nProject completed successfully!")