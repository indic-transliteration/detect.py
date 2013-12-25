detect.py
=========

When handling a Sanskrit string, it's almost always best to explicitly state
its transliteration scheme. This avoids embarrassing errors with words
like `pitRRIn`. But most of the time, it's possible to infer the encoding
from the text itself.

`detect.py` automatically detects a string's transliteration scheme:

    detect('pitRRIn') == 'itrans'
    detect('pitRRn') == 'hk'
    detect('pitFn') == 'slp1'
    detect('पितॄन्') == 'devanagari'
    detect('পিতৄন্') == 'bengali'

Supported schemes
-----------------

All schemes are attributes on the `Scheme` class. Or, just use the scheme name
as a lowercase string:

    Scheme.IAST == 'iast'

Scripts:

- Bengali (`Scheme.BENGALI`, `'bengali'`)
- Devanagari (`Scheme.DEVANAGARI`, `'devanagari'`)
- Gujarati (`Scheme.GUJARATI`, `'gujarati'`)
- Gurmukhi (`Scheme.GURMUKHI`, `'gurmukhi'`)
- Kannada (`Scheme.KANNADA`, `'kannada'`)
- Malayalam (`Scheme.MALAYALAM`, `'malayalam'`)
- Oriya (`Scheme.ORIYA`, `'oriya'`)
- Tamil (`Scheme.TAMIL`, `'tamil'`)
- Telugu (`Scheme.TELUGU`, `'telugu'`)

Romanizations:

- Harvard-Kyoto (`Scheme.HK`, `'hk'`)
- IAST (`Scheme.IAST`, `'iast'`)
- ITRANS (`Scheme.ITRANS`, `'itrans'`)
- Kolkata (`Scheme.KOLKATA`, `'kolkata'`)
- SLP1 (`Scheme.SLP1`, `'slp1'`)
- Velthuis (`Scheme.VELTHUIS`, `'velthuis'`)
