from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.utils.predictor import predict_tea_disease

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
    upload_path = f"backend/uploads/{file.filename}"

    with open(upload_path, "wb") as buffer:
        buffer.write(await file.read())

    result = predict_tea_disease(upload_path)
    return result