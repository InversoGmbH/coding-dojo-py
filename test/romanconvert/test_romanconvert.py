#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from romanconvertkata.romanconvert import roman2decimal
from unittest import TestCase


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
