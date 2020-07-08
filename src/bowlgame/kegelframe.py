#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.bowlexception import BowlToManyPins, BowlToManyShots


class KegelFrame:
    """Klasse für einen Durchgang beim Kegelspiel"""
    MAXIMUM_PINS = 9

    def shot(self, s):
        if s > self.pins:
            raise BowlToManyPins()
        if self.is_finished():
            raise BowlToManyShots()
        self.shots = self.shots + 1
        self.pins = self.pins - s

    def is_finished(self):
        return self.pins == 0 or self.shots >= 2

    def __init__(self):
        self.shots = 0
        self.pins = self.MAXIMUM_PINS
