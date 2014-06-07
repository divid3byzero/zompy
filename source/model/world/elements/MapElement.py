from source.model.base.BaseTile import BaseTile

__author__ = 'Sebastian'

import pygame
import os

class MapElement(BaseTile):

    def __init__(self, col, row, walkable):

        self.isWalkable = walkable
        if self.isWalkable:
            image = os.path.join("ressources", "images", "floor.jpg")
            print(image)
        else:
            image = os.path.join("ressources", "images", "wall.jpg")
            print(image)

        BaseTile.__init__(self, col, row, image)

