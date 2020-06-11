#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from romanconvertkata.RomanConvertException import RomanConvertException


def roman2decimal(roman: str) -> int:
    """
    Übersetzt eine Römische Zahl in ihren Dezimalwert

    :raises: :class:`RomanConvertException`: Fehler im übergebenen String
    :param roman: String mit Römischer Zahl
    :return: Dezimalwert der Römischen Zahl
    """
    ergebnis = 0
    for char in roman:
        if char == "i":
            ergebnis += 1
        if char == "v":
            ergebnis += 5
        if char == "l":
            ergebnis += 50
        if char == "d":
            ergebnis += 500
    return ergebnis
