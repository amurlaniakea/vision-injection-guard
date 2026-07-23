"""
Normalization Module: Normalize extracted text to handle unicode, homoglyphs, and adversarial spacing.
"""
import unicodedata
import re
from typing import Dict


def normalize_text(raw_text: str) -> str:
    """
    Normalize text by handling unicode, homoglyphs, and adversarial spacing.
    
    Args:
        raw_text: Raw text from OCR.
    
    Returns:
        Normalized text.
    """
    if not raw_text:
        return ""
    
    # Step 1: Normalize unicode (NFKC form)
    normalized = unicodedata.normalize("NFKC", raw_text)
    
    # Step 2: Replace homoglyphs with their standard counterparts
    homoglyph_map = get_homoglyph_map()
    for homoglyph, standard in homoglyph_map.items():
        normalized = normalized.replace(homoglyph, standard)
    
    # Step 3: Normalize whitespace and adversarial spacing
    normalized = re.sub(r'\s+', ' ', normalized)  # Replace multiple spaces with single space
    normalized = normalized.strip()
    
    return normalized


def get_homoglyph_map() -> Dict[str, str]:
    """
    Return a mapping of common homoglyphs to their standard counterparts.
    
    Returns:
        Dictionary mapping homoglyphs to standard characters.
    """
    return {
        # Cyrillic homoglyphs
        'а': 'a',  # Cyrillic 'a'
        'е': 'e',  # Cyrillic 'e'
        'о': 'o',  # Cyrillic 'o'
        'с': 'c',  # Cyrillic 'c'
        'р': 'p',  # Cyrillic 'p'
        'х': 'x',  # Cyrillic 'x'
        'у': 'y',  # Cyrillic 'y'
        'А': 'A',  # Cyrillic 'A'
        'Е': 'E',  # Cyrillic 'E'
        'О': 'O',  # Cyrillic 'O'
        'С': 'C',  # Cyrillic 'C'
        'Р': 'P',  # Cyrillic 'P'
        'Х': 'X',  # Cyrillic 'X'
        'У': 'Y',  # Cyrillic 'Y'
        
        # Greek homoglyphs
        'α': 'a',  # Greek alpha
        'ε': 'e',  # Greek epsilon
        'ο': 'o',  # Greek omicron
        'ρ': 'p',  # Greek rho
        'χ': 'x',  # Greek chi
        'υ': 'y',  # Greek upsilon
        
        # Other common homoglyphs
        'ａ': 'a',  # Fullwidth 'a'
        'ｅ': 'e',  # Fullwidth 'e'
        'ｏ': 'o',  # Fullwidth 'o'
        'ｃ': 'c',  # Fullwidth 'c'
        'ｐ': 'p',  # Fullwidth 'p'
        'ｘ': 'x',  # Fullwidth 'x'
        'ｙ': 'y',  # Fullwidth 'y'
    }
