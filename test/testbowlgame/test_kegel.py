#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import random

from bowlgame.bowlexception import BowlToManyShots, BowlToManyPins, BowlGameEnds
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

    def test_frame_change_zero_shot(self):
        """Null-Wurf beendet Frame und lässt Spiel einen neuen Erzeugen"""
        # Prepare
        old_frame = self.game.get_frame()
        old_frame.shot(0)
        new_frame = self.game.get_frame()

        # Test
        self.assertNotEqual(old_frame, new_frame)

    def test_frame_change_to_big_shot(self):
        """zu großer Wurf beendet Frame und lässt Spiel einen neuen Erzeugen"""
        # Prepare
        old_frame = self.game.get_frame()
        old_frame.shot(random.randint(4, MAXIMUM_PINS))
        new_frame = self.game.get_frame()

        # Test
        self.assertNotEqual(old_frame, new_frame)


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
