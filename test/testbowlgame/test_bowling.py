#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest import skip

from bowlgame.bowlexception import BowlToManyShots
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

    @skip
    def test_frame_change(self):
        """Null-Wurf beendet Frame und lässt Spiel einen neuen Erzeugen"""
        # Prepare
        old_frame = self.game.get_frame()
        old_frame.shot(0)
        old_frame2 = self.game.get_frame()
        old_frame.shot(0)
        new_frame = self.game.get_frame()

        # Test
        self.assertEqual(old_frame, old_frame2)
        self.assertNotEqual(old_frame, new_frame)


class BowlingFrameTestCase(AbstractBowlHelper.FrameHelper):
    """Testfälle für BowlingFrame"""

    def setUp(self):
        """Präpariert für jeden Test einen neuen Frame"""
        self.frame = BowlingFrame()
        self.maximum_pins = MAXIMUM_PINS

    def test_to_many_shots(self):
        """Exception-Test auf zuviele Würfe"""
        # prepare
        self.frame.shot(0)
        self.frame.shot(1)
        with self.assertRaises(BowlToManyShots):
            self.frame.shot(0)

    def test_no_second_shot(self):
        """Wurden beim ersten Wurf alle Kegel abgeräumt, gibt es keinen zweiten"""
        # prepare
        self.frame.shot(MAXIMUM_PINS)
        with self.assertRaises(BowlToManyShots):
            self.frame.shot(0)


if __name__ == '__main__':
    unittest.main()
