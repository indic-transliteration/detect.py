# -*- coding: utf-8 -*-
"""
    test
    ~~~~

    Tests for detect.py

    :license: MIT and BSD
"""

import pytest

from detect import detect, Scheme as S


def add(testcases, scheme, items):
    testcases.extend([(x, scheme) for x in items])


BASIC = []
add(BASIC, S.BENGALI, ['অ', '৺'])
add(BASIC, S.DEVANAGARI, ['ऄ', 'ॿ'])
add(BASIC, S.GUJARATI, ['અ', '૱'])
add(BASIC, S.GURMUKHI, ['ਅ', 'ੴ'])
add(BASIC, S.KANNADA, ['ಅ', '೯'])
add(BASIC, S.MALAYALAM, ['അ', 'ൿ'])
add(BASIC, S.ORIYA, ['ଅ', 'ୱ'])
add(BASIC, S.TAMIL, ['அ', '௺'])
add(BASIC, S.TELUGU, ['అ', '౿'])
add(BASIC, S.HK, [
    '',
    'rAga',
    'nadI',
    'vadhU',
    'kRta',
    'pitRRn',
    'klRpta',
    'lRR',
    'tejasvI',
    'gomayaH',
    'haMsa',
    'naraH',
    'aGga',
    'aJjana',
    'kuTumba',
    'kaThora',
    'Damaru',
    'soDhA',
    'aruNa',
    'zveta',
    'SaS',
    'pANDava',
    'zRNoti',
    'jJAna',
    'gacchati',
    'SaNmAsa',
    'pariNata',
    'aruNa',
    'reNu',
    'koNa',
    'karaNa',
    'akSa',
    'antazcarati',
    'prazna',
    'azvatthAman',
    'yuddha',
])
add(BASIC, S.IAST, [
    'rāga',
    'nadī',
    'vadhū',
    'kṛta',
    'pitṝn',
    'kḷpta',
    'ḹ',
    'tejasvī',
    'gomayaḥ',
    'haṃsa',
    'naraḥ',
    'aṅga',
    'añjana',
    'kuṭumba',
    'kaṭhora',
    'ḍamaru',
    'soḍhā',
    'aruṇa',
    'śveta',
    'ṣaṣ',
    'ḻa',
    'pāṇḍava',
    'śṛṇoti',
    'jñāna',
])
add(BASIC, S.ITRANS, [
    'raaga',
    'nadii',
    'nadee',
    'vadhuu',
    'vadhoo',
    'kRRita',
    'kR^ita',
    'pitRRIn',
    'pitR^In',
    'kLLipta',
    'kL^ipta',
    'LLI',
    'L^I',
    'a~Nga',
    'aN^ga',
    'ChAyA',
    'chhAyA',
    'a~njana',
    'aJNjana',
    'shveta',
    'ShaSh',
    'shhashh',
    '.akarot',
    'shRRiNoti',
    'j~nAna',
    'gachChati',
    'gachchhati',
])
add(BASIC, S.KOLKATA, [
    'tējas',
    'sōma',
])
add(BASIC, S.SLP1, [
    'kfta',
    'pitFn',
    'kxpta',
    'XkAra',
    'kEvalya',
    'kOsalya',
    'aNka',
    'aNga',
    'CAyA',
    'aYjana',
    'jYAna',
    'kuwumba',
    'kaWora'
    'qamaru',
    'soQA',
    'pARqava',
    'Pala',
    'Bara',
    'gacCati',
    'zaRmAsa',
    'pariRata',
    'aruRa',
    'SfRoti',
    'reRu',
    'koRa',
    'ArDadrORika',
    'akza',
    'antaScarati',
    'praSna',
    'aSvatTAman',
    'yudDa',
])
add(BASIC, S.VELTHUIS, [
    'k.rta',
    'pit.rrn',
    'k.lipta',
    '.ll',
    'sa.myoga',
    'gomaya.h',
    'a"nga',
    'ku.tumba',
    'ka.thora',
    '.damaru',
    'so.dhaa',
    'aru.na',
    '~sveta',
    '.sa.s',
])


@pytest.mark.parametrize('data', BASIC)
def test_basic(data):
    text, scheme = data
    detection = detect(text)
    assert detection == scheme, u'%s == %s (%s)' % (detection, scheme, text)


@pytest.mark.parametrize('data', BASIC)
def test_decoded(data):
    text, scheme = data
    text = text.decode('utf-8')
    detection = detect(text)
    assert detection == scheme, u'%s == %s (%s)' % (detection, scheme, text)


@pytest.mark.parametrize('data', BASIC)
def test_noisy(data):
    noise = ' \t\n 1234567890 !@#$%^&*(),.<>\'\"-_[]{}\\|;:`~ ΣД あア'
    text, scheme = data
    text = ''.join([noise, text, noise])
    assert detect(text) == scheme
