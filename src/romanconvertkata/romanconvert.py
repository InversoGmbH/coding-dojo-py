#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


def roman2decimal(roman: str) -> int:
    """
    Übersetzt eine Römische Zahl in ihren Dezimalwert

    :raises: :class:`RomanConvertException`: Fehler im übergebenen String
    :param roman: String mit Römischer Zahl
    :return: Dezimalwert der Römischen Zahl
    """
    roman = roman.upper()
    for c in roman:
        if c not in ROMAN_VALUES.keys():
            raise RomanConvertException(f"{c} from {roman} is not a roman number")

    result = 0
    previousValue = 0
    for c in roman:
        currentValue = ROMAN_VALUES[c]
        if previousValue < currentValue:
            result -= previousValue
            result -= previousValue
        result += currentValue

    return result
