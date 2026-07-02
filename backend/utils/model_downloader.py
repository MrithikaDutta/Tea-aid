import os
from huggingface_hub import hf_hub_download


REPO_ID = "MRIITHIIKA/TeaAid-models"

MODEL_DIR = "backend/models"

MODEL_FILES = [
    "best_efficientnet_b0.pt",
    "best_by_severity_mae.pt",
]


def download_models_if_missing():
    os.makedirs(MODEL_DIR, exist_ok=True)

    for filename in MODEL_FILES:
        local_path = os.path.join(MODEL_DIR, filename)

        if not os.path.exists(local_path):
            print(f"Downloading {filename} from Hugging Face...")

            downloaded_path = hf_hub_download(
                repo_id=REPO_ID,
                filename=filename,
                local_dir=MODEL_DIR,
                local_dir_use_symlinks=False,
            )

            print(f"Downloaded: {downloaded_path}")
        else:
            print(f"Model already exists: {filename}")
