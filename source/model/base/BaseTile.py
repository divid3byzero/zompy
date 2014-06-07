__author__ = 'Hanna'

import pygame
from abc import ABCMeta, abstractmethod

class BaseTile(pygame.Rect):
    __metaclass__ = ABCMeta

    WIDTH = 40
    HEIGHT = 40

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * BaseTile.WIDTH
        self.y = row * BaseTile.HEIGHT
        pygame.Rect.__init__(self, self.x, self.y, BaseTile.WIDTH, BaseTile.HEIGHT)

    @abstractmethod
    def draw(self, screen):
        pass