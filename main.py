#!/usr/bin/env python3

import curses

from game import Game

def main(stdscr):
    #stdscr.bkgd(' ', curses.color_pair(0))
    game = Game(stdscr)
    game.mainLoop()

if __name__ == '__main__':
    curses.wrapper(main)
