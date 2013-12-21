# -*- coding: utf-8 -*-
"""
    detect
    ~~~~~~

    Code for automatically detecting a transliteration scheme.

    :license: MIT and BSD
"""

#: Scheme data. This is split into separate classes, but here it's DRY.
SCHEMES = [
    ('devanagari', 0x0900),
    ('hk', None)
]

#: First code point for Brahmic scripts
BRAHMIC_CODE_POINT = 0x0900


class Scheme:

    """Contains the names of various Sanskrit schemes."""


for name, code in SCHEMES:
    setattr(Scheme, name.upper(), name)


def detect(text):
    """Detect the input's transliteration scheme

    :param text: some text data
    """
    if ord(text[0]) >= BRAHMIC_CODE_POINT:
        return Scheme.DEVANAGARI

    return Scheme.HK
