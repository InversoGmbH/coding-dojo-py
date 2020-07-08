#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.bowlexception import BowlToManyPins, BowlToManyShots


class KegelFrame:
    """Klasse für einen Durchgang beim Kegelspiel"""
    MAXIMUM_PINS = 9

    MAXIMUM_POINTS_PER_SHOT = 3

    def shot(self, s):
        if s > self.pins:
            raise BowlToManyPins()
        if self.finished:
            raise BowlToManyShots()
        if self.MAXIMUM_POINTS_PER_SHOT < s:
            self.finished = True
        else:
            self.points += s

    def is_finished(self):
        return self.finished

    def __init__(self):
        self.pins = self.MAXIMUM_PINS
        self.finished = False
        self.points = 0
