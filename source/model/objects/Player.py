__author__ = 'Sebastian'

import pygame
import os
from source.model.base.BaseTile import BaseTile
from source.model.base.Movable import Movable


class Player(Movable):

    IMAGE = pygame.image.load(os.path.join("resources", "images", "zombie", "zombie.png"))
    STEP_SIZE_WIDTH = BaseTile.WIDTH
    STEP_SIZE_HEIGHT = BaseTile.HEIGHT

    def __init__(self, row, col):
        Movable.__init__(self, row, col, Player.IMAGE)
        self.sprites = pygame.sprite.RenderPlain()
        self.sprites.add(self)
        print("Player: Initiale Position ist: x = {0}, y = {1}".format(self.rect.x, self.rect.y))

    def moveNorth(self):
        self.rect.y -= Player.STEP_SIZE_HEIGHT
        print("Player: y-Position = {0}".format(self.rect.y))

    def moveEast(self):
        self.rect.x += Player.STEP_SIZE_WIDTH

    def moveSouth(self):
        self.rect.y += Player.STEP_SIZE_HEIGHT

    def moveWest(self):
        self.rect.x -= Player.STEP_SIZE_WIDTH