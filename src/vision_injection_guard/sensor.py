"""
Sensor Module: Main entry point for the vision-injection-guard sensor.
"""
from typing import Dict
from .ocr import extract_text
from .normalize import normalize_text
from .detect import detect_injection


def process_image(image_path: str) -> Dict[str, str]:
    """
    Process an image to detect visually injected text.
    
    Args:
        image_path: Path to the image file.
    
    Returns:
        Dictionary with verdict, score, extracted_text, and normalized_text.
    """
    # Step 1: Extract text from image
    extracted_text = extract_text(image_path)
    
    # Step 2: Normalize the extracted text
    normalized_text = normalize_text(extracted_text)
    
    # Step 3: Detect injection
    detection_result = detect_injection(normalized_text)
    
    # Step 4: Return standard sensor output
    return {
        "verdict": detection_result["verdict"],
        "score": detection_result["score"],
        "extracted_text": extracted_text,
        "normalized_text": normalized_text,
    }
