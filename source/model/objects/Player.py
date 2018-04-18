__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

import os
import pygame
from model.base.Movable import Movable


class Player(Movable):
    """
    Class representing the player.
    """
    def __init__(self, pathToImage):
        """
        Constructor of the player.
        :param pathToImage: the image of the player
        """
        Movable.__init__(self, pathToImage)
        self.life = 100
        self.score = 0
        self.shotSound = pygame.mixer.Sound(os.path.join("resources", "sound", "shot.ogg"))

    def hit(self):
        """
        Called when the player is hit by a enemy. Reduces the players hitpoints.
        """
        self.life -= 0.5
        if self.life <= 0:
            self.kill()