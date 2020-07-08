#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.bowlexception import BowlToManyPins

MAXIMUM_PINS = 10


class BowlingFrame:
    """Klasse für einen Durchgang beim Bowlingspiel"""

    def shot(self, s):
        if s > MAXIMUM_PINS:
            raise BowlToManyPins()
