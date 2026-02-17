import os

# Capture
CAPTURE_INTERVAL = 60   # seconds
SCREENSHOT_DIR = "screenshots"

# OCR
OCR_LANG = "eng"
TESSERACT_CONFIG = r'--oem 3 --psm 11'

# Logs
LOG_DIR = "logs"
OCR_LOG_FILE = os.path.join(LOG_DIR, "ocr_log.jsonl")

# Ensure folders exist
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
