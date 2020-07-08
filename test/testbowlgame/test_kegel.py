#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from bowlgame.bowlexception import BowlToManyShots
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

    def test_to_many_shots(self):
        """Exception-Test auf zuviele Würfe"""
        # prepare
        self.frame.shot(MAXIMUM_PINS)
        with self.assertRaises(BowlToManyShots):
            self.frame.shot(MAXIMUM_PINS)

    def test_pin_recovery(self):
        """Pins sollen bei jedem Wurf zurück gesetzt werden"""
        try:
            for _ in range(0, MAXIMUM_PINS * 2):
                self.frame.shot(1)
        except Exception as e:
            self.fail("Beim Versuch von %i Einer-Würfen, kam es zu einem Fehler: %s" % (MAXIMUM_PINS * 2, str(e)))


if __name__ == '__main__':
    unittest.main()
