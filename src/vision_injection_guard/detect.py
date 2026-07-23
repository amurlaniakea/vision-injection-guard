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
