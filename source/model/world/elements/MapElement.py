from source.model.base.BaseTile import BaseTile

__author__ = 'Sebastian'

import pygame
import os

class MapElement(BaseTile):

    def __init__(self, image, walkable):
            BaseTile.__init__(self, image, walkable)