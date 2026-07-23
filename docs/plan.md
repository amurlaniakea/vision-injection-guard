# Plan: vision-injection-guard

## Milestones

### Milestone 1: Setup and Dependencies
- [ ] Create project structure (`src/`, `tests/`, `docs/`).
- [ ] Add `pytesseract` and `tesseract-ocr` to dependencies.
- [ ] Reuse `scope-lib/adi-shield` for injection detection.

### Milestone 2: Core OCR and Normalization
- [ ] Implement OCR extraction using Tesseract.
- [ ] Implement text normalization (unicode, homoglyphs, spacing).
- [ ] Write unit tests for OCR and normalization.

### Milestone 3: Injection Detection
- [ ] Integrate `scope-lib/adi-shield` detectors.
- [ ] Implement verdict logic (allow/flag/block).
- [ ] Write unit tests for detection.

### Milestone 4: Sensor Interface
- [ ] Implement standard sensor interface.
- [ ] Ensure output format matches ecosystem standards.
- [ ] Write integration tests.

### Milestone 5: Testing and Verification
- [ ] Run all tests (`pytest tests/ -v`).
- [ ] Check coverage (`coverage report`).
- [ ] Integrate with `agent-shield-runtime` for end-to-end test.

## Tasks

### Task 1: Project Setup
- Create `pyproject.toml` with dependencies.
- Add `pytesseract`, `scope-lib`, and `adi-shield`.
- Set up `src/vision_injection_guard/__init__.py`.

### Task 2: OCR Module
- Implement `src/vision_injection_guard/ocr.py`:
  - Function: `extract_text(image_path: str) -> str`.
  - Use `pytesseract.image_to_string`.
- Write tests in `tests/test_ocr.py`.

### Task 3: Normalization Module
- Implement `src/vision_injection_guard/normalize.py`:
  - Function: `normalize_text(raw_text: str) -> str`.
  - Handle unicode, homoglyphs, and adversarial spacing.
- Write tests in `tests/test_normalize.py`.

### Task 4: Detection Module
- Implement `src/vision_injection_guard/detect.py`:
  - Function: `detect_injection(normalized_text: str) -> dict`.
  - Integrate `scope-lib/adi-shield` detectors.
  - Return `verdict`, `score`.
- Write tests in `tests/test_detect.py`.

### Task 5: Sensor Module
- Implement `src/vision_injection_guard/sensor.py`:
  - Function: `process_image(image_path: str) -> dict`.
  - Orchestrate OCR → Normalize → Detect.
  - Return standard sensor output format.
- Write tests in `tests/test_sensor.py`.

### Task 6: Integration Test
- Write `tests/test_integration.py`:
  - Test full pipeline with sample images.
  - Verify output format matches ecosystem standards.

### Task 7: Verification
- Run `pytest tests/ -v` and paste raw output.
- Run `coverage report` and paste raw output.
- Ensure all tests pass and coverage >= 90%.
