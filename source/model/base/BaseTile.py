__author__ = 'Hanna'

import pygame
from abc import ABCMeta, abstractmethod

class BaseTile(pygame.sprite.Sprite):
    __metaclass__ = ABCMeta

    WIDTH = 48
    HEIGHT = 48

    def __init__(self, row, col, image):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = self.__loadImage(image)
        self.rect = self.image.get_rect()
        self.rect.x = col * BaseTile.WIDTH
        self.rect.y = row * BaseTile.HEIGHT

    def __loadImage(self, image):
        if image.get_width() is not BaseTile.WIDTH or image.get_height() is not BaseTile.HEIGHT:
            image = pygame.transform.scale(self.image, (BaseTile.WIDTH, BaseTile.HEIGHT))
        return image