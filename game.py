#!/usr/bin/env python3

import curses

from player import Player
from enums import Direction

class Game:

    def __init__(self, screen):

        self.screen = screen
        self.running = True
        self.player = Player()
        self.border = 1

    def keep_in_border(self, mob):
        minY, minX = [coordinate + self.border for coordinate in
                self.screen.getbegyx()]
        maxY, maxX = [coordinate - self.border - 1 for coordinate in
                self.screen.getmaxyx()]
        
        if mob.x < minX:
            mob.x = minX
        elif mob.x > maxX:
            mob.x = maxX
        if mob.y < minY:
            mob.y = minY
        elif mob.y > maxY:
            mob.y = maxY

    def mainLoop(self):
        while(self.running):
            self.logic()
            self.draw()
            self.handleInput()

    def logic(self):
        self.keep_in_border(self.player)
        
    def draw(self):
        self.screen.erase()
        self.screen.border('|', '|', '-', '-', '+', '+', '+', '+')
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
