__author__ = 'Sebastian'

import pygame
from source.algo.Pathfinder import Pathfinder
from source.model.base.Movable import Movable


class Enemy(Movable):

    def __init__(self, pathToImage):
        Movable.__init__(self, pathToImage)
        self.pathfinder = Pathfinder()