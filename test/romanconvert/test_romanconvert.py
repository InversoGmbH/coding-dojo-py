#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from romanconvertkata.romanconvert import roman2decimal
from unittest import TestCase
import math


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

    def test_einser(self):
        """i, ii und iii als Eingabeparameter"""
        self.assertEqual(1, roman2decimal('i'))
        self.assertEqual(2, roman2decimal('ii'))
        self.assertEqual(3, roman2decimal('iii'))

    def test_fuenfer_potenzen(self):
        """v, l, d als Eingabeparameter"""
        self.assertEqual(5, roman2decimal('v'))
        self.assertEqual(50, roman2decimal('l'))
        self.assertEqual(500, roman2decimal('d'))

    def test_zehner_potenzen(self):
        """x, xx, xxx, c, cc, ccc, m, mm und mmm als Eingabeparameter"""
        self.assertEqual(10, roman2decimal('x'))
        self.assertEqual(20, roman2decimal('xx'))
        self.assertEqual(30, roman2decimal('xxx'))
        self.assertEqual(100, roman2decimal('c'))
        self.assertEqual(200, roman2decimal('cc'))
        self.assertEqual(300, roman2decimal('ccc'))
        self.assertEqual(1000, roman2decimal('m'))
        self.assertEqual(2000, roman2decimal('mm'))
        self.assertEqual(3000, roman2decimal('mmm'))

    def test_subtraktionsregel(self):
        """iv, ix, xl, xc, cd, cm als Eingabeparameter"""
        self.assertEqual(4, roman2decimal('iv'))
        self.assertEqual(9, roman2decimal('ix'))
        self.assertEqual(40, roman2decimal('xl'))
        self.assertEqual(90, roman2decimal('xc'))
        self.assertEqual(400, roman2decimal('cd'))
        self.assertEqual(900, roman2decimal('cm'))

    def test_kombination(self):
        """Kombiniere diverse römische Ziffern zu einer Zahl"""
        self.assertEqual(8, roman2decimal('viii'))
        self.assertEqual(42, roman2decimal('xlii'))
        self.assertEqual(99, roman2decimal('xcix'))
        self.assertEqual(2020, roman2decimal('mmxx'))

    def test_random_kombination(self):
        """Randomzahlen zwischen 1 und 3999 prüfen"""
        for i in range(1, 100):
            zahl = random.randint(i, 3999)
            self.assertEqual(roman2decimal(_create_roman(zahl)), zahl)