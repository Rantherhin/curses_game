#!/usr/bin/python

import curses

from player import Player
from enums import Direction

class Game:

    def __init__(self, screen):

        self.screen = screen
        self.running = True
        self.player = Player()

    def mainLoop(self):
        while(self.running):
            self.logic()
            self.draw()
            self.handleInput()

    def logic(self):
        pass

    def draw(self):
        self.screen.erase()
        player = self.player
        self.screen.addch(player.y, player.x, player.character,
                curses.color_pair(1))
        self.screen.move(player.y, player.x)
        self.screen.refresh()

    def handleInput(self):
        character = self.screen.getch()
        if 0 < character < 256:
            character = chr(character)
            if character in 'q':
                self.running = False
            elif character in 'h':
                self.player.move(Direction.LEFT)
            elif character in 'j':
                self.player.move(Direction.DOWN)
            elif character in 'k':
                self.player.move(Direction.UP)
            elif character in 'l':
                self.player.move(Direction.RIGHT)
        else:
            pass
