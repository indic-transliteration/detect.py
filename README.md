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

- Bengali (`Scheme.BENGALI`)
- Devanagari (`Scheme.DEVANAGARI`)
- Gujarati (`Scheme.GUJARATI`)
- Gurmukhi (`Scheme.GURMUKHI`)
- Kannada (`Scheme.KANNADA`)
- Malayalam (`Scheme.MALAYALAM`)
- Oriya (`Scheme.ORIYA`)
- Tamil (`Scheme.TAMIL`)
- Telugu (`Scheme.TELUGU`)

Romanizations:

- Harvard-Kyoto (`Scheme.HK`)
- IAST (`Scheme.IAST`)
- ITRANS (`Scheme.ITRANS`)
- Kolkata (`Scheme.KOLKATA`)
- SLP1 (`Scheme.SLP1`)
- Velthuis (`Scheme.VELTHUIS`)
