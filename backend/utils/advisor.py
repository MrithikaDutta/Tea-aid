def get_treatment_advice(disease: str, severity_grade: str):
    disease = disease.lower()

    if disease == "healthy":
        return (
            "The tea leaf appears healthy. No disease treatment is required. "
            "Continue regular monitoring, maintain proper field hygiene, ensure balanced irrigation, "
            "and avoid unnecessary chemical application."
        )

    advice_data = {
        "algal_leaf_spot": {
            "Mild": "Mild algal leaf spot is detected. Remove a few affected leaves if necessary, improve air circulation, reduce excess moisture, and monitor the plant regularly.",
            "Moderate": "Moderate algal leaf spot is detected. Prune affected leaves, improve drainage and sunlight exposure, avoid prolonged leaf wetness, and monitor nearby plants for spread.",
            "Severe": "Severe algal leaf spot is detected. Remove heavily infected leaves, improve field sanitation, reduce humidity around plants, and consult local agricultural experts for suitable control measures.",
        },
        "brown_blight": {
            "Mild": "Mild brown blight is detected. Remove infected leaves, avoid overhead watering, and monitor the plant for symptom progression.",
            "Moderate": "Moderate brown blight is detected. Prune infected parts, improve air circulation, maintain field hygiene, and avoid prolonged moisture on leaves.",
            "Severe": "Severe brown blight is detected. Remove severely infected leaves, isolate affected plant areas if possible, improve sanitation, and consult agricultural experts for proper disease management.",
        },
        "gray_blight": {
            "Mild": "Mild gray blight is detected. Remove early infected leaves, keep the field clean, and avoid excess moisture.",
            "Moderate": "Moderate gray blight is detected. Prune infected areas, improve ventilation, reduce leaf wetness, and monitor disease spread carefully.",
            "Severe": "Severe gray blight is detected. Remove heavily infected leaves, improve field sanitation, and seek local agricultural guidance for suitable treatment.",
        },
        "helopeltis": {
            "Mild": "Mild helopeltis damage is detected. Monitor young shoots and leaves regularly and remove damaged parts if needed.",
            "Moderate": "Moderate helopeltis damage is detected. Inspect nearby plants, remove damaged shoots, maintain field hygiene, and follow recommended pest management practices.",
            "Severe": "Severe helopeltis damage is detected. Conduct regular field inspection, remove severely damaged shoots, and consult local agricultural experts for appropriate pest control measures.",
        },
    }

    return advice_data.get(disease, {}).get(
        severity_grade,
        "Monitor the plant carefully and consult local agricultural experts for suitable treatment advice."
    )