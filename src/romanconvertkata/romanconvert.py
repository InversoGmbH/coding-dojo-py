#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re
from romanconvertkata.RomanConvertException import RomanConvertException

logger = logging.getLogger('romanconvertkata')

fehler_syntax = "Eingabe '{0}' beinhaltet syntaktische Fehler"
fehler_semantik = "Eingabe '{0}' beinhaltet semantische Fehler"


def roman2decimal(roman: str) -> int:
    """
    Übersetzt eine Römische Zahl in ihren Dezimalwert

    :raises: :class:`RomanConvertException`: Fehler im übergebenen String
    :param roman: String mit Römischer Zahl
    :return: Dezimalwert der Römischen Zahl
    """
    __pruefe_eingabe(roman)
    zahlen = __gib_arabische_ziffern(roman)
    laenge = len(roman)
    zahl = 0
    for i in range(0, laenge):
        wert = zahlen[i]
        if i > 0 and zahlen[i - 1] < (wert / 10):
            raise RomanConvertException(fehler_semantik.format(roman))

        if i < (laenge - 1) and zahlen[i + 1] > wert:
            zahl -= wert
        else:
            zahl += wert

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


def __gib_arabische_ziffern(numerus_romanus: str):
    """
    Erzeugen einer Liste von Zahlen für die römischen Ziffern
    """

    def __romanus2arabicus(r):
        try:
            return numeri_romani[r]
        except KeyError:
            raise RomanConvertException(fehler_syntax.format(numerus_romanus))

    roemische_zahl = numerus_romanus.upper()
    zahlen = list(map(__romanus2arabicus, roemische_zahl))
    return zahlen


def __pruefe_eingabe(eingabe):
    if eingabe == None:
        raise RomanConvertException('Es wurde keine Eingabe übergeben')

    if not isinstance(eingabe, str):
        raise RomanConvertException(fehler_syntax.format(eingabe))

    if len(eingabe) == 0:
        raise RomanConvertException('Es wurde keine Eingabe übergeben')

    if re.findall("I{4,}|V{2,}|X{4,}|L{2,}|C{4,}|D{2,}|M{4,}|ↁL{2,}", eingabe.upper()):
        raise RomanConvertException(fehler_semantik.format(eingabe))

    if eingabe.isalpha() and not (eingabe.islower() or eingabe.isupper()):
        logger.warning(
            "Groß- und Kleinschreibung wurden in der Eingabe '{0}' vermischt".format(eingabe))

    return

# print(roman2decimal('IC'))
