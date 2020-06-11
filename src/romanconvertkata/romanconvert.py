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
    # print( roman )
    fehlermeldung = __pruefe_eingabe(roman)
    zahlen = __gib_arabische_ziffern(roman, fehlermeldung)
    laenge = len(roman)
    zahl = 0
    for i in range(0, laenge - 1):
        wert = zahlen[i]
        wert_nachfolger = zahlen[i + 1]
        if wert_nachfolger > wert:
            zahl -= wert
        else:
            zahl += wert

    zahl += zahlen[laenge - 1]
    return zahl


numeri_romani = {
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


def __gib_arabische_ziffern(numerus_romanus: str, fehlermeldung: str):
    """
    Erzeugen einer Liste von Zahlen für die römischen Ziffern
    """

    def __romanus2arabicus(r):
        try:
            return numeri_romani[r]
        except KeyError:
            raise RomanConvertException(fehlermeldung.format(numerus_romanus))

    roemische_zahl = numerus_romanus.upper()
    zahlen = list(map(__romanus2arabicus, roemische_zahl))
    return zahlen


def __pruefe_eingabe(eingabe):
    fehlermeldung = "Eingabe {0} beinhaltet syntaktische Fehler"
    if not isinstance(eingabe, str):
        raise RomanConvertException(fehlermeldung.format(eingabe))
    return fehlermeldung
