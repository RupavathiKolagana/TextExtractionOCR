import pytesseract
import cv2
from PIL import Image

# Path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image = cv2.imread("meme_image.jpeg")

if image is None:
    print("❌ Error: Image not found. Check file name/path.")
else:
    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Extract text
    extracted_text = pytesseract.image_to_string(img_rgb)

    print("✅ Extracted Text:")
    print(extracted_text)
