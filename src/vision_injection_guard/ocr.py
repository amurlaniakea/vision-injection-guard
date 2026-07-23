"""
OCR Module: Extract text from images using Tesseract.
"""
import pytesseract
from PIL import Image
from typing import Optional


def extract_text(image_path: str) -> str:
    """
    Extract text from an image using Tesseract OCR.
    
    Args:
        image_path: Path to the image file.
    
    Returns:
        Extracted text as a string.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract to extract text
            text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from image: {e}")
