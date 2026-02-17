import cv2
import pytesseract
from PIL import Image
from .config import OCR_LANG, TESSERACT_CONFIG

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # upscale image (helps small fonts)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=2.0, beta=0)

    # adaptive threshold (better for UI text)
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 2
    )

    return thresh

def extract_text(image_path):
    processed = preprocess_image(image_path)
    pil_img = Image.fromarray(processed)

    text = pytesseract.image_to_string(
        pil_img,
        lang=OCR_LANG,
        config=TESSERACT_CONFIG
    )

    # Basic cleaning
    text = text.strip()
    text = " ".join(text.split())

    return text
