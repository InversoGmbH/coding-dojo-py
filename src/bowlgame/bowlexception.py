#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BowlToManyShots(Exception):
    """Fehler, der geworfen wird, wenn in einem Frame mehr Würfe gemacht werden, als erlaubt"""


class BowlToManyPins(Exception):
    """Fehler, der geworfen wird, wenn zuviele Pins umgeworfen wurden"""


class BowlGameEnds(Exception):
    """Fehler, der geworfen wird, wenn das Spiel beendet wurde und ein neuer Frame angefordert wird"""
