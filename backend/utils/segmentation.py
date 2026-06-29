import os
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from transformers import SegformerForSemanticSegmentation


MODEL_PATH = "backend/models/best_by_severity_mae.pt"
DEVICE = torch.device("cpu")

checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)

IMG_SIZE = checkpoint["img_size"]
NUM_CLASSES = checkpoint["num_classes"]

model = SegformerForSemanticSegmentation.from_pretrained(
    "nvidia/segformer-b0-finetuned-ade-512-512",
    num_labels=NUM_CLASSES,
    ignore_mismatched_sizes=True,
)

model.load_state_dict(checkpoint["model_state_dict"])
model.to(DEVICE)
model.eval()

transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])


def get_severity_grade(severity_percentage: float):
    if severity_percentage == 0:
        return "Healthy"
    elif severity_percentage <= 15:
        return "Mild"
    elif severity_percentage <= 40:
        return "Moderate"
    else:
        return "Severe"


def save_mask_image(predicted_mask, original_filename):
    os.makedirs("backend/static/masks", exist_ok=True)

    mask_rgb = np.zeros((predicted_mask.shape[0], predicted_mask.shape[1], 3), dtype=np.uint8)

# Background pixels = soft charcoal gray
    mask_rgb[predicted_mask == 0] = [48, 52, 50]

# Disease pixels = bright amber/orange highlight
    mask_rgb[np.isin(predicted_mask, [1, 2, 3, 4])] = [255, 170, 30]

# Leaf pixels = dark muted green
    mask_rgb[predicted_mask == 5] = [42, 95, 68]

    mask_image = Image.fromarray(mask_rgb)

    filename = os.path.basename(original_filename)
    mask_filename = f"mask_{filename}.png"
    mask_path = os.path.join("backend/static/masks", mask_filename)

    mask_image.save(mask_path)

    return f"/static/masks/{mask_filename}"

def estimate_severity(image_path: str):
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(pixel_values=image_tensor)
        logits = outputs.logits

        logits = torch.nn.functional.interpolate(
            logits,
            size=(IMG_SIZE, IMG_SIZE),
            mode="bilinear",
            align_corners=False,
        )

        predicted_mask = torch.argmax(logits, dim=1).squeeze().cpu().numpy()

    infected_pixels = np.isin(predicted_mask, [1, 2, 3, 4]).sum()
    leaf_pixels = (predicted_mask == 5).sum()

    total_leaf_area = infected_pixels + leaf_pixels

    if total_leaf_area == 0:
        severity_percentage = 0.0
    else:
        severity_percentage = (infected_pixels / total_leaf_area) * 100

    severity_grade = get_severity_grade(severity_percentage)
    mask_url = save_mask_image(predicted_mask, image_path)

    return severity_percentage, severity_grade, mask_url