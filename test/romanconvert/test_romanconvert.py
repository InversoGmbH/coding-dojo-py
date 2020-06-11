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