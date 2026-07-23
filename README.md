# vision-injection-guard

A deterministic, CPU-only sensor for detecting visually injected text in images before they reach a VLM. Part of the agent-shield-runtime ecosystem.

## Features
- OCR-based text extraction using Tesseract (CPU-only).
- Text normalization for unicode, homoglyphs, and adversarial spacing.
- Integration with existing prompt injection detectors from scope-lib/adi-shield.
- Standard sensor output format (verdict, score, extracted text).

## Installation

```bash
pip install vision-injection-guard
```

## Usage

```python
from vision_injection_guard import process_image

result = process_image("path/to/image.png")
print(result)
# {"verdict": "allow", "score": 0.0, "extracted_text": "...", "normalized_text": "..."}
```

## License

AGPL-3.0-or-later
