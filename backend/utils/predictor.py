def predict_tea_disease(filename: str):
    """
    Temporary demo prediction function.
    Later we will replace this with the real trained models.
    """

    result = {
        "filename": filename,
        "disease": "Brown Blight",
        "confidence": "95.16%",
        "severity_percentage": "23.50%",
        "severity_grade": "Moderate",
        "advice": (
            "Remove infected leaves, improve air circulation, avoid overhead "
            "watering, and monitor disease spread regularly."
        ),
    }

    return result