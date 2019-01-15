#!/usr/bin/env python3

from enums import Direction

class Player:
    
    def __init__(self):
        self.x = 20
        self.y = 20
        self.character = '@'

    def move(self, direction):
        if direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.DOWN:
            self.y += 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.RIGHT:
            self.x += 1
