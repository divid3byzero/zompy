__author__ = 'bene'


from source.model.theming.AbstractThemeFactory import AbstractThemeFactory
from source.model.objects.Player import Player
from source.model.world.elements.FloorTile import FloorTile
from source.model.world.elements.WallTile import WallTile
import os
import pygame
class GrasslandsThemeFactory(AbstractThemeFactory):

    def __init__(self):
        self.__walkableImage = pygame.image.load(os.path.join("resources", "images", "map", "grass.png"))
        self.__notWalkableImage = pygame.image.load(os.path.join("resources", "images", "map", "wall_grey.png"))
        self.__playerImage = pygame.image.load(os.path.join("resources", "images", "zombie", "zombie.png"))

    def _createWall(self):
        return WallTile(self.__notWalkableImage)

    def _createFloor(self):
        return FloorTile(self.__walkableImage)

    def _createPlayer(self):
        return Player(self.__playerImage)
