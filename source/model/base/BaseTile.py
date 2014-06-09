__author__ = 'Hanna'

import pygame
from abc import ABCMeta, abstractmethod

class BaseTile(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    WIDTH = 48
    HEIGHT = 48

    def __init__(self, pathToImage, walkable):
        pygame.sprite.Sprite.__init__(self)
        self.isWalkable = walkable
        self.image = self.__loadImage(pathToImage)
        self.rect = self.image.get_rect()

    def __loadImage(self, pathToImage):
        image = pygame.image.load(pathToImage)
        if image.get_width() is not BaseTile.WIDTH or image.get_height() is not BaseTile.HEIGHT:
            image = pygame.transform.scale(self.image, (BaseTile.WIDTH, BaseTile.HEIGHT))
        return image

    def setCoordinates(self, row, col):
        self.row = row
        self.col = col
        self.rect.x = col * BaseTile.WIDTH
        self.rect.y = row * BaseTile.HEIGHT