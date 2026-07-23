"""
Detection Module: Detect prompt injection in normalized text using scope-lib/adi-shield.
"""
from typing import Dict

# Import the real detection function from adi-shield
from adi_shield.detector import score_masquerade


def detect_injection(normalized_text: str) -> Dict[str, float]:
    """
    Detect prompt injection in normalized text using adi-shield's real detection.
    
    Args:
        normalized_text: Normalized text from OCR.
    
    Returns:
        Dictionary with 'verdict' and 'score'.
    """
    if not normalized_text:
        return {"verdict": "allow", "score": 0.0}
    
    # Use the real adi-shield detection function
    score = score_masquerade(normalized_text)
    
    # Determine verdict based on score (matching adi-shield's logic)
    # score_masquerade returns only 0.0 or 0.9, so we only have two cases
    if score >= 0.9:
        verdict = "block"
    else:
        verdict = "allow"
    
    return {"verdict": verdict, "score": round(score, 2)}
