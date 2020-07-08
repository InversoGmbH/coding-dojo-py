#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from functools import reduce

from romanconvertkata.RomanConvertException import RomanConvertException

ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "ↁ": 5000,
    "ↂ": 10000
}


def hasInvalidCountOfNumber(roman: str) -> bool:
    count = 0
    previousC = ''
    for c in roman:
        if c != previousC:
            count = 0
        count += 1
        if count > 3:
            return True
    return False


def hasInvalidCountOfFiveValue(roman: str) -> bool:
    FIVER = ["V", "L", "D", "ↁ"]
    count = 0
    previousC = ''
    for c in roman:
        if c != previousC:
            count = 0
        count += 1
        if count > 1 and c in FIVER:
            return True
    return False


def containsUppaerAndLower(roman: str) -> bool:
    upperRomans = ROMAN_VALUES.keys()
    lowerRomans = [x.lower() for x in upperRomans]
    reduceOr = lambda x, y: x or y
    containsUpper = reduce(reduceOr, [x != "ↁ" and x != "ↂ" and x in upperRomans for x in roman])
    containsLower = reduce(reduceOr, [x != "ↁ" and x != "ↂ" and x in lowerRomans for x in roman])
    return containsUpper and containsLower


def roman2decimal(roman: str) -> int:
    """
    Übersetzt eine Römische Zahl in ihren Dezimalwert

    :raises: :class:`RomanConvertException`: Fehler im übergebenen String
    :param roman: String mit Römischer Zahl
    :return: Dezimalwert der Römischen Zahl
    """
    log = logging.getLogger("romanconvertkata")

    if roman == '' or roman == None:
        raise RomanConvertException("Es wurde keine Eingabe übergeben")

    if type(roman) is not str:
        raise RomanConvertException(f"Eingabe {roman} beinhaltet syntaktische Fehler")

    for c in roman.upper():
        if c not in ROMAN_VALUES.keys():
            raise RomanConvertException(f"Eingabe {roman} beinhaltet syntaktische Fehler")

    if containsUppaerAndLower(roman):
        log.warning(f"Groß- und Kleinschreibung wurden in der Eingabe {roman} vermischt")


    roman = roman.upper()

    if hasInvalidCountOfNumber(roman) or hasInvalidCountOfFiveValue(roman):
        raise RomanConvertException(f"Eingabe {roman} beinhaltet semantische Fehler")

    result = 0
    previousValue = 0
    for c in roman:
        currentValue = ROMAN_VALUES[c]
        if previousValue < currentValue:
            result -= previousValue
            result -= previousValue
        result += currentValue
        previousValue = currentValue
    return result
