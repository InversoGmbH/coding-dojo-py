#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from bowlgame.bowlingframe import BowlingFrame
from bowlgame.bowlinggame import BowlingGame
from test.testbowlgame.helper import AbstractBowlHelper

MAXIMUM_PINS = 10
"""Maximal umzuschießende Pins"""


class BowlingGameTestCase(AbstractBowlHelper.GameHelper):
    """Testfälle für BowlingGame"""

    def setUp(self):
        """Präpariert für jeden Test ein neues Spiel und einen neuen Frame"""
        # Wird für abstrakte Testfälle in helper.AbstractBowlHelper.GameHelper benötigt
        self.game = BowlingGame()
        self.frame = BowlingFrame()


class BowlingFrameTestCase(AbstractBowlHelper.FrameHelper):
    """Testfälle für BowlingFrame"""

    def setUp(self):
        """Präpariert für jeden Test einen neuen Frame"""
        self.frame = BowlingFrame()
        self.maximum_pins = MAXIMUM_PINS


if __name__ == '__main__':
    unittest.main()
