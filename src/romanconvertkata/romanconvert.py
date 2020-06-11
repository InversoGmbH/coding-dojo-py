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
    #print( roman )
    ergebnis = 0
    previous = None
    for char in roman.lower():
        if char == "i":
            ergebnis += 1
        elif char == "v":
            if previous == "i":
                ergebnis += 3
                continue
            ergebnis += 5
        elif char == "l":
            if previous == "x":
                ergebnis += 30
                continue
            ergebnis += 50
        elif char == "d":
            if previous == "c":
                ergebnis += 300
                continue
            ergebnis += 500
        elif char == "x":
            if previous == "i":
                ergebnis += 8
                continue
            ergebnis += 10
        elif char == "c":
            if previous == "x":
                ergebnis += 80
                continue
            ergebnis += 100
        elif char == "m":
            if previous == "c":
                ergebnis += 800
                continue
            ergebnis += 1000
        elif char == "ↁ":
            if previous == "m":
                ergebnis+= 5000-2000
                continue
            else:
                ergebnis += 5000
            continue
        elif char == "ↂ":
            if previous == "m":
                ergebnis += 10000 - 2000
                continue
            else:
                ergebnis += 10000
                continue
        else:
            raise RomanConvertException("Keine gültige Zeichen")
        previous = char
    return ergebnis
