#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from bowlgame.bowlingframe import BowlingFrame
from bowlgame.bowlinggame import BowlingGame
from test.testbowlgame.helper import AbstractBowlHelper


class BowlingGameTestCase(AbstractBowlHelper.GameHelper):
    """Testfälle für BowlingGame"""

    def setUp(self):
        """Präpariert für jeden Test ein neues Spiel und einen neuen Frame"""
        # Wird für abstrakte Testfälle in helper.AbstractBowlHelper.GameHelper benötigt
        self.game = BowlingGame()
        self.frame = BowlingFrame()


if __name__ == '__main__':
    unittest.main()
