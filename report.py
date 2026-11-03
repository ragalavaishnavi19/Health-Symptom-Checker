from datetime import datetime


def generate_report(
    name,
    age,
    gender,
    symptoms,
    symptom_names,
    disease,
    confidence
):

    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    filename = "health_report.txt"

    with open(filename, "w") as file:

        file.write("=" * 50 + "\n")
        file.write("PATIENT DETAILS\n")
        file.write("=" * 50 + "\n\n")

        file.write(f"Name         : {name}\n")
        file.write(f"Age          : {age}\n")
        file.write(f"Gender       : {gender}\n")
        file.write(f"Date         : {current_date}\n")
        file.write(f"Time         : {current_time}\n\n")

        file.write("=" * 50 + "\n")
        file.write("AI HEALTH SYMPTOM CHECKER REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write("Symptoms Entered:\n")

        for i in range(len(symptoms)):
            if symptoms[i] == 1:
                file.write(f"- {symptom_names[i]}\n")

        file.write("\n")

        file.write(f"Predicted Disease : {disease}\n")
        file.write(f"Confidence Score  : {confidence}%\n\n")

        file.write("AI Recommendation\n")
        file.write("---------------------------\n")

        recommendations = {
            "Flu": "Drink plenty of water, take rest and consult a doctor if fever continues.",
            "Cold": "Stay warm, drink warm fluids and take proper rest.",
            "COVID-19": "Isolate yourself and consult a healthcare professional.",
            "Dengue": "Drink more fluids and visit a healthcare professional.",
            "Malaria": "Consult a doctor and take prescribed medicines.",
            "Migraine": "Take rest in a quiet room and avoid bright light.",
            "Typhoid": "Take antibiotics only under medical supervision.",
            "Sinusitis": "Use steam inhalation and consult a doctor if symptoms persist.",
            "Pneumonia": "Seek immediate medical attention.",
            "Influenza": "Take adequate rest and drink plenty of fluids.",
            "Allergy": "Avoid allergens and consult a doctor if required.",
            "Stress": "Take rest, exercise regularly and maintain a healthy lifestyle.",
            "Viral Fever": "Drink fluids, take rest and monitor your temperature."
        }

        file.write(
            recommendations.get(
                disease,
                "Please consult a healthcare professional for proper diagnosis."
            )
        )

    print("\nHealth Report Saved Successfully!")