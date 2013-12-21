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
