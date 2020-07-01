#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from bowlgame.bowlexception import BowlToManyPins


class AbstractBowlHelper(object):
    """Abstrakte-Verdeckungsklasse um Helperklassen vor unittest-discovery zu verstecken"""
    class GameHelper(unittest.TestCase):
        """Helper-Klasse für Game-Klassen-Tests"""

        def test_initial_score(self):
            """Methode get_score() exisitert und gibt initial 0 zurück"""
            self.assertEqual(self.game.get_score(), 0)

        def test_initial_is_frame(self):
            """Methode is_frame() exisitert und gibt initial 1 zurück"""
            self.assertEqual(self.game.is_frame(), 1)

        def test_initial_get_frame(self):
            """Methode get_frame() exisitert und gibt einen Frame zurück"""
            self.assertIsInstance(self.game.get_frame(), type(self.frame))

    class FrameHelper(unittest.TestCase):
        """Helper-Klasse für Game-Klassen-Tests"""

        def test_zero_shot(self):
            """Methode shot() exisitert"""
            try:
                self.frame.shot(0)
            except Exception as e:
                self.fail("Es konnte kein 0-Wurf ausgeführt werden. Exception: %s" % str(e))

        def test_to_many_pins(self):
            """Exception-Test auf zuviele Pins beim Wurf"""
            with self.assertRaises(BowlToManyPins):
                self.frame.shot(self.maximum_pins + 1)

