# -*- coding: utf-8 -*-
"""
    detect
    ~~~~~~

    Code for automatically detecting a transliteration scheme.

    :license: MIT and BSD
"""

import re

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
    ('hk', None),
    ('iast', None),
    ('itrans', None),
    ('kolkata', None),
    ('slp1', None),
    ('velthuis', None),
]

#: Start of the Devanagari block.
BRAHMIC_FIRST_CODE_POINT = 0x0900

#: End of the Malayalam block.
BRAHMIC_LAST_CODE_POINT = 0x0d7f

#: Schemes sorted by Unicode code point. Ignore schemes with none defined.
BLOCKS = sorted([x for x in SCHEMES if x[-1]], key=lambda x: -x[1])

#: Enum for Sanskrit schemes.
Scheme = type('Enum', (), {name.upper() : name for name, code in SCHEMES})


class Regex:

    #: Match on special Roman characters
    IAST_OR_KOLKATA_ONLY = re.compile(ur'[āīūṛṝḷḹēōṃḥṅñṭḍṇśṣ]')

    #: Match on chars shared by ITRANS and Velthuis
    ITRANS_OR_VELTHUIS_ONLY = re.compile(ur'aa|ii|uu|~n')

    #: Match on ITRANS-only
    ITRANS_ONLY = re.compile(ur'\^[iI]|R[iI]|L[iI]|~N|Ch|chh|sh|Sh')

    #: Match on Kolkata-specific Roman characters
    KOLKATA_ONLY = re.compile(ur'[ēō]')

    #: Match on SLP1-only characters and bigrams
    SLP1_ONLY = re.compile(ur'[fFxXEOCYwWqQ]|Nk|Ng|kz|' \
                           ur'[aAiIuUfFxXeEoO]R')

    #: Match on Velthuis-only characters
    VELTHUIS_ONLY = re.compile(ur'\.r|\.l|[".]n|\.t|\.d|[~\.]s')


def detect(text, default=Scheme.HK):
    """Detect the input's transliteration scheme.

    :param text: some text data
    """

    # Brahmic schemes are all within a specific range of code points.
    for L in text:
        code = ord(L)
        if code >= BRAHMIC_FIRST_CODE_POINT:
            for name, start_code in BLOCKS:
                if start_code <= code <= BRAHMIC_LAST_CODE_POINT:
                    return name

    # Romanizations
    if Regex.IAST_OR_KOLKATA_ONLY.search(text):
        if Regex.KOLKATA_ONLY.search(text):
            return Scheme.KOLKATA
        else:
            return Scheme.IAST

    if Regex.ITRANS_ONLY.search(text):
        return Scheme.ITRANS

    if Regex.SLP1_ONLY.search(text):
        return Scheme.SLP1

    if Regex.VELTHUIS_ONLY.search(text):
        return Scheme.VELTHUIS

    if Regex.ITRANS_OR_VELTHUIS_ONLY.search(text):
        return Scheme.ITRANS

    return default
