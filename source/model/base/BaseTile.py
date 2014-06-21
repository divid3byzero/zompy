__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import pygame
from abc import ABCMeta

class BaseTile(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    WIDTH = 48
    HEIGHT = 48

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.row = None
        self.col = None

    def setCoordinates(self, row, col):
        self.row = row
        self.col = col
        self.rect.x = col * BaseTile.WIDTH
        self.rect.y = row * BaseTile.HEIGHT