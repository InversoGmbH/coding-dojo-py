#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from romanconvertkata.RomanConvertException import RomanConvertException
from romanconvertkata.romanconvert import roman2decimal
from unittest import TestCase
import logging
import math
import random


def _create_roman(zahl: int) -> str:
    """
    Übersetzt Dezimalzahl in Römische Zahl

    :param zahl: Dezimalzahl
    :return: Römische Zahl
    """
    romans_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "ↁ",
        10000: "ↂ"
    }

    div = 1
    while zahl >= div:
        div *= 10

    div /= 10

    res = ""

    while zahl:
        last_num = int(zahl / div)
        if last_num <= 3:
            res += (romans_dict[div] * last_num)
        elif last_num == 4:
            res += (romans_dict[div] +
                    romans_dict[div * 5])
        elif 5 <= last_num <= 8:
            res += (romans_dict[div * 5] +
                    (romans_dict[div] * (last_num - 5)))
        elif last_num == 9:
            res += (romans_dict[div] +
                    romans_dict[div * 10])

        zahl = math.floor(zahl % div)
        div /= 10

    return res


class TestRomanConvert(TestCase):

    def assertEqualRoman(self, erwartet: int, eingabe: str):
        self.assertEqual(erwartet, roman2decimal(eingabe),
                         msg="roman2decimal(%s) != %i, erhaltener Rückgabewert: %i" %
                             (eingabe, erwartet, roman2decimal(eingabe)))

    def test_einser(self):
        """i, ii und iii als Eingabeparameter"""
        self.assertEqualRoman(1, 'i')
        self.assertEqualRoman(2, 'ii')
        self.assertEqualRoman(3, 'iii')

    def test_fuenfer_potenzen(self):
        """v, l, d als Eingabeparameter"""
        self.assertEqualRoman(5, 'v')
        self.assertEqualRoman(50, 'l')
        self.assertEqualRoman(500, 'd')

    def test_zehner_potenzen(self):
        """x, xx, xxx, c, cc, ccc, m, mm und mmm als Eingabeparameter"""
        self.assertEqualRoman(10, 'x')
        self.assertEqualRoman(20, 'xx')
        self.assertEqualRoman(30, 'xxx')
        self.assertEqualRoman(100, 'c')
        self.assertEqualRoman(200, 'cc')
        self.assertEqualRoman(300, 'ccc')
        self.assertEqualRoman(1000, 'm')
        self.assertEqualRoman(2000, 'mm')
        self.assertEqualRoman(3000, 'mmm')

    def test_subtraktionsregel(self):
        """iv, ix, xl, xc, cd, cm als Eingabeparameter"""
        self.assertEqualRoman(4, 'iv')
        self.assertEqualRoman(9, 'ix')
        self.assertEqualRoman(40, 'xl')
        self.assertEqualRoman(90, 'xc')
        self.assertEqualRoman(400, 'cd')
        self.assertEqualRoman(900, 'cm')

    def test_kombination(self):
        """Kombiniere diverse römische Ziffern zu einer Zahl"""
        self.assertEqualRoman(8, 'viii')
        self.assertEqualRoman(42, 'xlii')
        self.assertEqualRoman(99, 'xcix')
        self.assertEqualRoman(2020, 'mmxx')

    def test_random_kombination(self):
        """Randomzahlen zwischen 1 und 3999 prüfen"""
        for i in range(1, 100):
            zahl = random.randint(i, 3999)
            self.assertEqual(roman2decimal(_create_roman(zahl)), zahl)

    def test_ulkige_zeichen(self):
        """Tests für ↁ und ↂ"""
        self.assertEqualRoman(5000, 'ↁ')
        self.assertEqualRoman(10000, 'ↂ')
        self.assertEqualRoman(4000, 'mↁ')
        self.assertEqualRoman(9000, 'mↂ')
        self.assertEqualRoman(39999, 'ↂↂↂmↂcmxcix')

    def test_random_kombination_ulkige_zeichen(self):
        """Randomzahlen zwischen 4000 und 39999 prüfen"""
        for i in range(0, 100):
            zahl = random.randint(i + 4000, 39999)
            self.assertEqual(roman2decimal(_create_roman(zahl)), zahl)

    def test_unbekannte_zeichen_uebergeben(self):
        """Syntaktische Fehler sollen :class:`RomanConvertException` werfen"""
        self._syntaktischer_fehler('abc')
        self._syntaktischer_fehler(123)
        self._syntaktischer_fehler({'1': 'x'})

    def _syntaktischer_fehler(self, roman: str):
        with self.assertRaisesRegexp(RomanConvertException, "Eingabe '%s' beinhaltet syntaktische Fehler" % roman):
            roman2decimal(roman)

    def test_semantischer_fehler(self):
        """Semantische Fehler sollen :class:`RomanConvertException` werfen"""
        self._semantischer_fehler('IC')
        self._semantischer_fehler('IIIII')
        self._semantischer_fehler('VV')

    def _semantischer_fehler(self, roman: str):
        with self.assertRaisesRegexp(RomanConvertException, "Eingabe '%s' beinhaltet semantische Fehler" % roman):
            roman2decimal(roman)

    def test_fehlende_eingabe(self):
        """Fehlende Eingabe soll eine :class:`RomanConvertException` erzeugen"""
        self._fehlende_eingabe('')
        self._fehlende_eingabe(None)

    def _fehlende_eingabe(self, roman: str):
        with self.assertRaisesRegexp(RomanConvertException, 'Es wurde keine Eingabe übergeben'):
            roman2decimal(roman)

    def test_gross_und_kleinschreibung(self):
        """Warning 'Groß- und Kleinschreibung wurden in der Eingabe %s vermischt' wird erwartet

        Solange alle Buchstaben nur in Klein- oder Großschreibung übertragen werden, soll die Konvertierung normal von
        statten gehen. Sobald Groß- und Kleinbuchstaben gemischt sind, soll dem Logger 'romanconvertkata' ein Warning
        übergeben werden.
        """
        log = logging.getLogger('romanconvertkata')
        eingabe = 'mmxx'
        with self.assertLogs('romanconvertkata', level=logging.WARNING) as cm:
            self.assertEqual(2020, roman2decimal(eingabe))
            log.warning('dummy')
        self.assertEqual(cm.output, ['WARNING:romanconvertkata:dummy'],
                         'Es darf kein Warning bei mmxx geschrieben werden')
        eingabe = 'MMXX'
        with self.assertLogs('romanconvertkata', level=logging.WARNING) as cm:
            self.assertEqual(2020, roman2decimal(eingabe))
            log.warning('dummy')
        self.assertEqual(cm.output, ['WARNING:romanconvertkata:dummy'],
                         'Es darf kein Warning bei MMXX geschrieben werden')
        eingabe = 'mmXX'
        with self.assertLogs('romanconvertkata', level=logging.WARNING) as cm:
            self.assertEqual(2020, roman2decimal(eingabe))
        warning = "WARNING:romanconvertkata:Groß- und Kleinschreibung wurden in der Eingabe '%s' vermischt" % eingabe
        self.assertIn(warning, cm.output, "Die Warnmeldung '%s' wurde nicht im Logger registriert." % warning)
