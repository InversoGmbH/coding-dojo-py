#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.bowlexception import BowlToManyPins, BowlToManyShots

MAXIMUM_PINS = 10


class BowlingFrame:
    """Klasse für einen Durchgang beim Bowlingspiel"""

    def shot(self, s):
        if s > self.pins:
            raise BowlToManyPins()
        self.shots = self.shots + 1
        if self.shots > 2:
            raise BowlToManyShots()
        if self.pins == 0:
            raise BowlToManyShots()
        self.pins = self.pins - s

    def __init__(self):
        self.shots = 0
        self.pins = MAXIMUM_PINS
