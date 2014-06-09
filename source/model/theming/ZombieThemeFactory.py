__author__ = 'bene'

from source.model.theming.AbstractThemeFactory import AbstractThemeFactory
from source.model.objects.Player import Player
from source.model.world.elements.MapElement import MapElement
import os
import pygame
import copy
class ZombieThemeFactory(AbstractThemeFactory):


    def __init__(self):
        self.__walkableImage = pygame.image.load(os.path.join("resources", "images", "map", "mud.png"))
        self.__notWalkableImage = pygame.image.load(os.path.join("resources", "images", "map", "wall.png"))
        self.__playerImage = pygame.image.load(os.path.join("resources", "images", "zombie", "zombie.png"))

    def createWall(self):
        return MapElement(self.__notWalkableImage, False)

    def createFloor(self):
        return MapElement(self.__walkableImage, True)

    def createPlayer(self):
        return Player(self.__playerImage)