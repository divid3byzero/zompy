__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import pygame
from abc import ABCMeta


class BaseTile(pygame.sprite.Sprite):
    """
    Abstract class providing the base functionality of all game components (tiles)
    """
    __metaclass__ = ABCMeta

    WIDTH = 48
    HEIGHT = 48

    def __init__(self, image):
        """
        Constructor of the base class
        :param image: the image of this tile
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.row = None
        self.col = None

    def setCoordinates(self, row, col):
        """
        Sets the coordinates calculated by the row and column of this tile
        :param row: the row in which this tile is stored
        :param col: the column in which this tile is stored
        """
        self.row = row
        self.col = col
        self.rect.x = col * BaseTile.WIDTH
        self.rect.y = row * BaseTile.HEIGHT