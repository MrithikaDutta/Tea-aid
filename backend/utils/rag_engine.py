RAG_KNOWLEDGE_BASE = {
    "brown_blight": {
        "Mild": (
            "Remove visible infected leaves during routine field sanitation. "
            "Improve air circulation and avoid prolonged leaf wetness. "
            "Monitor nearby leaves weekly. If disease pressure is high, consider a preventive locally registered copper/contact fungicide according to label."
        ),
        "Moderate": (
            "Remove and destroy infected leaf material. "
            "Improve drainage, shade balance, and pruning to reduce humidity. "
            "Use a locally registered fungicide program appropriate for tea, rotating modes of action. "
            "Recheck after 7-14 days and record spread."
        ),
        "Severe": (
            "Consult tea extension, agronomist, or BTRI for confirmation. "
            "Prune heavily affected shoots or sections if needed. "
            "Use registered contact/systemic fungicide strategy according to label and pre-harvest interval. "
            "Increase monitoring frequency until new growth is healthy."
        ),
    },

    "gray_blight": {
        "Mild": (
            "Increase monitoring during wet periods. "
            "Remove small affected leaves if practical. "
            "Improve air movement through pruning and spacing. "
            "Maintain balanced nutrition, especially potassium."
        ),
        "Moderate": (
            "Remove infected material and reduce field humidity. "
            "Avoid working in wet fields where spread can increase. "
            "Use locally registered fungicide for tea blight diseases according to label. "
            "Re-inspect after 7-14 days."
        ),
        "Severe": (
            "Seek expert confirmation because severe gray blight can spread quickly. "
            "Prune severely affected growth where appropriate. "
            "Use a registered fungicide plan and rotate active ingredient groups. "
            "Maintain strict sanitation of tools and removed material."
        ),
    },

    "algal_leaf_spot": {
        "Mild": (
            "Improve sunlight penetration and airflow through pruning. "
            "Reduce excessive shade and moisture. "
            "Remove heavily affected older leaves where practical. "
            "Monitor after rain or humid periods."
        ),
        "Moderate": (
            "Combine cultural control with a locally registered copper-based product if recommended for tea. "
            "Correct drainage and shade problems. "
            "Avoid prolonged wet leaf surface. "
            "Recheck in 2-3 weeks because algal problems respond slowly."
        ),
        "Severe": (
            "Consult expert or extension service to confirm algal infection. "
            "Use registered copper-based control only as allowed locally. "
            "Prune heavily affected shaded sections and improve field hygiene. "
            "Monitor new growth for recurrence."
        ),
    },

    "helopeltis": {
        "Mild": (
            "Scout young shoots and surrounding bushes for active bugs or fresh feeding spots. "
            "Remove badly damaged shoots during plucking where practical. "
            "Improve shade regulation and field sanitation. "
            "Avoid unnecessary insecticide if damage is old and pest is not active."
        ),
        "Moderate": (
            "Increase monitoring of tender flushes and nearby sections. "
            "Remove alternate hosts or weeds around affected sections where recommended. "
            "Use IPM first: sanitation, shade management, drainage, and timely plucking. "
            "If active pest pressure is confirmed, use locally registered selective insecticide only according to label and extension guidance."
        ),
        "Severe": (
            "Consult a tea pest specialist or extension service quickly. "
            "Mark the affected block and monitor edge rows because spread may start at field margins. "
            "Consider targeted treatment only with locally registered products and PPE. "
            "Recheck after 7-10 days and avoid repeated unsupervised spraying."
        ),
    },

    "healthy": {
        "Healthy": (
            "No treatment is required. Continue routine monitoring, good drainage, balanced nutrition, sanitation, and disease-preventive field hygiene."
        )
    },
}


def retrieve_rag_chunk(disease: str, severity_grade: str):
    disease = disease.lower()

    if disease == "healthy":
        return RAG_KNOWLEDGE_BASE["healthy"]["Healthy"]

    disease_chunks = RAG_KNOWLEDGE_BASE.get(disease)

    if not disease_chunks:
        return "Monitor the plant carefully and consult local agricultural experts for suitable treatment advice."

    return disease_chunks.get(
        severity_grade,
        "Use severity-specific cultural control, sanitation, monitoring, and locally registered treatment only when needed."
    )


def generate_rag_advice(disease: str, severity_grade: str, severity_percent: float, confidence: float):
    disease = disease.lower()
    retrieved_advice = retrieve_rag_chunk(disease, severity_grade)

    if disease == "healthy":
        return (
            f"Disease: Healthy\n"
            f"Severity: Healthy ({severity_percent:.2f}%)\n"
            f"Likely issue: No visible disease class was detected.\n"
            f"Recommended action: {retrieved_advice}\n"
            f"Safety note: Do not apply pesticide unnecessarily."
        )

    confidence_note = ""
    if confidence < 70:
        confidence_note = (
            "\nConfidence note: The model confidence is low. Please verify with a clearer image or local expert before treatment."
        )

    return (
        f"Disease: {disease.replace('_', ' ').title()}\n"
        f"Severity: {severity_grade} ({severity_percent:.2f}%)\n"
        f"Likely issue: The model detected {disease.replace('_', ' ')} symptoms, and severity was estimated from infected pixel area.\n"
        f"Recommended action: {retrieved_advice}\n"
        f"Safety note: Use only locally registered products when needed. Follow label instructions, PPE, BTRI/extension guidance, and pre-harvest interval."
        f"{confidence_note}"
    )