#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bowlgame.kegelframe import KegelFrame


class KegelGame:
    """Klasse für ein Kegelspiel, welches aus KegelFrames besteht."""
    def __init__(self):
        self.frame = KegelFrame()

    def get_score(self):
        return 0

    def is_frame(self):
        return 1

    def get_frame(self):
        if self.frame.is_finished():
            self.frame = KegelFrame()
        return self.frame
