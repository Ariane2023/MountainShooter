#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.examples.grid import WINDOW_WIDTH, WINDOW_HEIGHT

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324)) #WINDOW_WIDTH, WINDOW_HEIGHT



    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass





