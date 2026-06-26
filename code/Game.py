#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Const import MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324)) #WINDOW_WIDTH, WINDOW_HEIGHT



    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit() # close window
                quit() # end game
            else:
                pass






