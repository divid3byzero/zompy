__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import os
import pygame
from source.model.base.Movable import Movable


class Player(Movable):

    def __init__(self, pathToImage):
        Movable.__init__(self, pathToImage)
        self.life = 100
        self.score = 0
        self.shotSound = pygame.mixer.Sound(os.path.join("resources", "sound", "shot.ogg"))

    def hit(self):
        self.life -= 0.5
        if self.life <= 0:
            self.kill()