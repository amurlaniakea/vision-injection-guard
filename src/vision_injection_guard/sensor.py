# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# Copyright (C) 2026 Pedro Sordo Martínez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program. If not, see
# <https://www.gnu.org/licenses/>.

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
