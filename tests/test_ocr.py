"""
Tests for OCR module.
"""
import pytest
from unittest.mock import patch, MagicMock
from vision_injection_guard.ocr import extract_text


def test_extract_text_with_clean_image():
    """Test OCR extraction with a clean image containing benign text."""
    # Mock both Image.open and pytesseract.image_to_string
    with patch('vision_injection_guard.ocr.Image.open') as mock_open:
        with patch('vision_injection_guard.ocr.pytesseract.image_to_string') as mock_ocr:
            # Create a mock image
            mock_img = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_img
            mock_ocr.return_value = "Hello World"
            
            result = extract_text("dummy_path.png")
            assert result == "Hello World"


def test_extract_text_with_no_text_image():
    """Test OCR extraction with an image containing no text."""
    with patch('vision_injection_guard.ocr.Image.open') as mock_open:
        with patch('vision_injection_guard.ocr.pytesseract.image_to_string') as mock_ocr:
            mock_img = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_img
            mock_ocr.return_value = ""
            
            result = extract_text("dummy_path.png")
            assert result == ""


def test_extract_text_with_invalid_path():
    """Test OCR extraction with an invalid image path."""
    with patch('vision_injection_guard.ocr.Image.open') as mock_open:
        mock_open.side_effect = FileNotFoundError("File not found")
        
        with pytest.raises(RuntimeError):
            extract_text("/invalid/path/to/image.png")
