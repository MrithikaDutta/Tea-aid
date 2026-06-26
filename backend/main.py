from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Tea-aid backend is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "disease": "Brown Blight",
        "confidence": "95.16%",
        "severity_percentage": "23.50%",
        "severity_grade": "Moderate",
        "advice": "Remove infected leaves, improve air circulation, avoid overhead watering, and monitor disease spread regularly."
    }