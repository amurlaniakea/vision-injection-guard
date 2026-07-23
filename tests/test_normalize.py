"""
Tests for normalization module.
"""
import pytest
from vision_injection_guard.normalize import normalize_text, get_homoglyph_map


def test_normalize_text_with_clean_text():
    """Test normalization with clean text."""
    raw_text = "Hello World"
    normalized = normalize_text(raw_text)
    assert normalized == "Hello World"


def test_normalize_text_with_unicode():
    """Test normalization with unicode characters."""
    raw_text = "Héllø Wörld"
    normalized = normalize_text(raw_text)
    assert normalized == "Héllø Wörld"  # Unicode should be preserved in NFKC form


def test_normalize_text_with_homoglyphs():
    """Test normalization with homoglyphs."""
    # Test individual homoglyph replacements
    homoglyph_map = get_homoglyph_map()
    
    # Test Cyrillic 'o' (U+043E)
    raw_text = "test\u043e"
    normalized = normalize_text(raw_text)
    assert normalized == "testo"  # Should replace Cyrillic 'o' with ASCII 'o'
    
    # Test Cyrillic 'a' (U+0430)
    raw_text = "test\u0430"
    normalized = normalize_text(raw_text)
    assert normalized == "testa"  # Should replace Cyrillic 'a' with ASCII 'a'
    
    # Test Cyrillic 'p' (U+0440)
    raw_text = "test\u0440"
    normalized = normalize_text(raw_text)
    assert normalized == "testp"  # Should replace Cyrillic 'p' with ASCII 'p'


def test_normalize_text_with_adversarial_spacing():
    """Test normalization with adversarial spacing."""
    raw_text = "Hello   World  \n  This is a test"
    normalized = normalize_text(raw_text)
    assert normalized == "Hello World This is a test"


def test_normalize_text_with_empty_input():
    """Test normalization with empty input."""
    raw_text = ""
    normalized = normalize_text(raw_text)
    assert normalized == ""


def test_get_homoglyph_map():
    """Test that homoglyph map contains expected mappings."""
    homoglyph_map = get_homoglyph_map()
    assert 'а' in homoglyph_map  # Cyrillic 'a'
    assert homoglyph_map['а'] == 'a'
    assert 'о' in homoglyph_map  # Cyrillic 'o'
    assert homoglyph_map['о'] == 'o'
