import torch
from PIL import Image
from torchvision import models, transforms


MODEL_PATH = "backend/models/best_efficientnet_b0.pt"
DEVICE = torch.device("cpu")

checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
CLASS_NAMES = checkpoint["class_names"]

model = models.efficientnet_b0(weights=None)
model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, len(CLASS_NAMES))
model.load_state_dict(checkpoint["model_state_dict"])
model.to(DEVICE)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])


def classify_image(image_path: str):
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted_index = torch.max(probabilities, 1)

    predicted_class = CLASS_NAMES[predicted_index.item()]
    confidence_score = confidence.item() * 100

    return predicted_class, confidence_score