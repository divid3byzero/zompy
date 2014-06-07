__author__ = 'Sebastian'

import pygame
from source.model.base.Movable import Movable


class Player(Movable):

    def __init__(self, row, col, image):
        Movable.__init__(self, row, col, image)

    def moveNorth(self):
        self.y = self.y - 10

    def moveEast(self):
        self.x = self.x + 10

    def moveSouth(self):
        self.y =  self.y + 10

    def moveWest(self):
        self.x = self.x - 10