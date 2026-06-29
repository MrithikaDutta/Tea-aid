from backend.utils.classification import classify_image
from backend.utils.segmentation import estimate_severity
from backend.utils.advisor import get_treatment_advice
from backend.utils.rag_engine import generate_rag_advice

def format_class_name(class_name: str):
    return class_name.replace("_", " ").title()


def get_demo_advice(disease: str, severity_grade: str):
    advice_map = {
        "healthy": "The leaf appears healthy. Continue regular monitoring, maintain good field hygiene, and avoid unnecessary chemical treatment.",
        "algal_leaf_spot": f"{severity_grade} algal leaf spot detected. Remove affected leaves if needed, improve air circulation, reduce excess moisture, and monitor nearby plants.",
        "brown_blight": f"{severity_grade} brown blight detected. Remove infected leaves, improve air circulation, avoid overhead watering, and monitor disease spread regularly.",
        "gray_blight": f"{severity_grade} gray blight detected. Prune infected parts, keep the field clean, avoid prolonged leaf wetness, and follow local agricultural guidance if symptoms increase.",
        "helopeltis": f"{severity_grade} helopeltis damage detected. Inspect plants regularly, remove damaged shoots if needed, and follow recommended pest management practices from local agricultural experts.",
    }

    return advice_map.get(
        disease,
        "Monitor the plant carefully and consult local agricultural experts for suitable treatment advice.",
    )


def predict_tea_disease(image_path: str):
    disease, confidence = classify_image(image_path)
    severity_percentage, severity_grade, mask_url = estimate_severity(image_path)
    if disease == "healthy":
        severity_percentage = 0.0
        severity_grade = "Healthy"

    if confidence < 70:
        warning = "Low confidence prediction. Please verify the result manually or use a clearer leaf image."
    else:
        warning = "Prediction confidence is acceptable."

    result = {
        "disease": format_class_name(disease),
        "confidence": f"{confidence:.2f}%",
        "severity_percentage": f"{severity_percentage:.2f}%",
        "severity_grade": severity_grade,
        "warning": warning,
        "mask_url": mask_url,
        "advice": generate_rag_advice(disease, severity_grade, severity_percentage, confidence),
    }

    return result