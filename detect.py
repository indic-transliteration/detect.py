# -*- coding: utf-8 -*-
"""
    detect
    ~~~~~~

    Code for automatically detecting a transliteration scheme.

    :license: MIT and BSD
"""

#: Scheme data. This is split into separate classes, but here it's DRY.
SCHEMES = [
    ('bengali', 0x0980),
    ('devanagari', 0x0900),
    ('gujarati', 0x0a80),
    ('gurmukhi', 0x0a00),
    ('kannada', 0x0c80),
    ('malayalam', 0x0d00),
    ('oriya', 0x0b00),
    ('tamil', 0x0b80),
    ('telugu', 0x0c00),
    ('hk', None)
]

#: First code point for Brahmic scripts
BRAHMIC_FIRST_CODE_POINT = 0x0900

#: Last code point for Brahmic scripts
BRAHMIC_LAST_CODE_POINT = 0x0d7f


#: Schemes sorted by Unicode code point. Ignore schemes with none defined.
BLOCKS = sorted([x for x in SCHEMES if x[-1]], key=lambda x: -x[1])



class Scheme:

    """Contains the names of various Sanskrit schemes."""


for name, code in SCHEMES:
    setattr(Scheme, name.upper(), name)


def detect(text):
    """Detect the input's transliteration scheme

    :param text: some text data
    """
    for L in text:
        code = ord(L)
        if code >= BRAHMIC_FIRST_CODE_POINT:
            for name, start_code in BLOCKS:
                if start_code <= code <= BRAHMIC_LAST_CODE_POINT:
                    return name

    return Scheme.HK
