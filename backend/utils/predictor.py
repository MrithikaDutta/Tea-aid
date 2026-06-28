from backend.utils.classification import classify_image


def format_class_name(class_name: str):
    return class_name.replace("_", " ").title()


def get_demo_advice(disease: str):
    advice_map = {
        "healthy": "The leaf appears healthy. Continue regular monitoring, maintain good field hygiene, and avoid unnecessary chemical treatment.",
        "algal_leaf_spot": "Remove severely affected leaves, improve air circulation, reduce excess moisture, and monitor nearby plants for spread.",
        "brown_blight": "Remove infected leaves, improve air circulation, avoid overhead watering, and monitor disease spread regularly.",
        "gray_blight": "Prune infected parts, keep the field clean, avoid prolonged leaf wetness, and follow local agricultural guidance if symptoms increase.",
        "helopeltis": "Inspect plants regularly, remove damaged shoots if needed, and follow recommended pest management practices from local agricultural experts.",
    }

    return advice_map.get(
        disease,
        "Monitor the plant carefully and consult local agricultural experts for suitable treatment advice.",
    )


def predict_tea_disease(image_path: str):
    disease, confidence = classify_image(image_path)

    if confidence < 70:
        warning = "Low confidence prediction. Please verify the result manually or use a clearer leaf image."
    else:
        warning = "Prediction confidence is acceptable."

    result = {
        "disease": format_class_name(disease),
        "confidence": f"{confidence:.2f}%",
        "severity_percentage": "23.50%",
        "severity_grade": "Moderate",
        "warning": warning,
        "advice": get_demo_advice(disease),
    }

    return result