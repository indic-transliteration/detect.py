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
    ('hk', None),
    ('iast', None),
    ('kolkata', None),
]

#: Start of the Devanagari block.
BRAHMIC_FIRST_CODE_POINT = 0x0900

#: End of the Malayalam block.
BRAHMIC_LAST_CODE_POINT = 0x0d7f

#: Schemes sorted by Unicode code point. Ignore schemes with none defined.
BLOCKS = sorted([x for x in SCHEMES if x[-1]], key=lambda x: -x[1])

#: Enum for Sanskrit schemes.
Scheme = type('Enum', (), {name.upper() : name for name, code in SCHEMES})


def _make_signature():
    all_tokens = {
        'iast': u'ā ī ū ṛ ṝ ḷ ḹ ṃ ḥ ṅ ñ ṭ ḍ ṇ ś ṣ'.split(),
        'kolkata': u'ā ī ū ṛ ṝ ḷ ḹ ē ō ṃ ḥ ṅ ñ ṭ ḍ ṇ ś ṣ'.split(),
    }

    signature = {}
    for scheme, tokens in all_tokens.iteritems():
        for t in tokens:
            signature.setdefault(t, []).append(scheme)
    return signature

#: Maps some token to the schemes that produce it.
SIGNATURE = _make_signature()

#: Orders schemes from most to least favorable. This is used when a scheme
#: is encoded ambiguously.
DEFAULT_RANKS = [
    Scheme.HK,
    Scheme.IAST,
    Scheme.KOLKATA
]


def likeliest(candidates, ranks=None):
    """Returns the likeliest choice from a set of candidates:

    :param candidates: a set of candidates
    :param ranks: an ordering over schemes, from most to least likely.
                  If ``None``, use `DEFAULT_RANKS` instead.
    """
    ranks = ranks or DEFAULT_RANKS
    for r in ranks:
        if r in candidates:
            return r
    return None


def detect(text):
    """Detect the input's transliteration scheme

    :param text: some text data
    """
    candidates = set(name for (name, code) in SCHEMES)

    for L in text:
        # Brahmic schemes are all within a specific range of code points.
        code = ord(L)
        if code >= BRAHMIC_FIRST_CODE_POINT:
            for name, start_code in BLOCKS:
                if start_code <= code <= BRAHMIC_LAST_CODE_POINT:
                    return name

        # Romanizations
        bottleneck = SIGNATURE.get(L, [])
        if bottleneck:
            new_candidates = candidates.intersection(bottleneck)
            if len(new_candidates) == 1:
                return list(new_candidates)[0]
            candidates = new_candidates

    return likeliest(candidates)
