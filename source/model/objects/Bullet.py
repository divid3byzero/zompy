__author__ = 'bene'

import pygame
import os
from source.model.base.Movable import Movable


class Bullet(Movable):

    def __init__(self):
        Movable.__init__(self, pygame.image.load(os.path.join("resources", "images", "hero", "bullet.png")))
        self.velocity = 8