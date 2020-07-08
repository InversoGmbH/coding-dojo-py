#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.bowlingframe import BowlingFrame


class BowlingGame:
    """Klasse für ein Bowlingspiel, welches aus 10 BowlingFrames besteht."""

    def __init__(self):
        self.frame = BowlingFrame()

    def get_score(self):
        return 0

    def is_frame(self):
        return 1

    def get_frame(self):
        if self.frame.is_finished():
            self.frame = BowlingFrame()
        return self.frame
