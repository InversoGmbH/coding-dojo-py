#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from romanconvertkata.romanconvert import roman2decimal
from unittest import TestCase


class TestRomanConvert(TestCase):

    def test_einser(self):
        """i, ii und iii als Eingabeparameter"""
        self.assertEqual(roman2decimal('i'), 1)
        self.assertEqual(roman2decimal('ii'), 2)
        self.assertEqual(roman2decimal('iii'), 3)
