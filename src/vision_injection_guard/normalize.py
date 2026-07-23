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