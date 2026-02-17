import json
from .config import OCR_LOG_FILE

def save_ocr_log(timestamp, text, image_path):
    if not text:
        return

    record = {
        "timestamp": timestamp,
        "text": text,
        "image": image_path
    }

    with open(OCR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
