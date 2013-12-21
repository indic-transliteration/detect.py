# -*- coding: utf-8 -*-
"""
    test
    ~~~~

    Tests for detect.py

    :license: MIT and BSD
"""

import pytest

from detect import detect, Scheme

BASIC_DATA = []


def add_basic_data(scheme, items):
    BASIC_DATA.extend([(x, scheme) for x in items])


add_basic_data(Scheme.DEVANAGARI, [
    'अ',
    'ॿ'
])


add_basic_data(Scheme.HK, [
    'a',
    'b',
    'c'
])


@pytest.mark.parametrize('data', BASIC_DATA)
def test_basic(data):
    text, scheme = data
    text = text.decode('utf-8')
    assert detect(text) == scheme
