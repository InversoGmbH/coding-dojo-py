#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from bowlgame.kegelframe import KegelFrame
from bowlgame.kegelgame import KegelGame
from test.testbowlgame.helper import AbstractBowlHelper

MAXIMUM_PINS = 9
"""Maximal umzuschießénde Pins"""

WINNING_SCORE = 25
"""Ergebnis ab dem ein Spiel gewonnen ist"""


class KegelGameTestCase(AbstractBowlHelper.GameHelper):
    """Testfälle für KegelGame"""

    def setUp(self):
        """Präpariert für jeden Test ein neues Spiel und einen neuen Frame"""
        # Wird für abstrakte Testfälle in helper.AbstractBowlHelper.GameHelper benötigt
        self.game = KegelGame()
        self.frame = KegelFrame()


class KegelFrameTestCase(AbstractBowlHelper.FrameHelper):
    """Testfälle für KegelFrame"""

    def setUp(self):
        """Präpariert für jeden Test einen neuen Frame"""
        self.frame = KegelFrame()
        self.maximum_pins = MAXIMUM_PINS


if __name__ == '__main__':
    unittest.main()
