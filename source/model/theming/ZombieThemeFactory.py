__author__ = 'bene'

from source.model.theming.AbstractThemeFactory import AbstractThemeFactory
from source.model.objects.Player import Player
from source.model.world.elements.MapElement import MapElement
import os
class ZombieThemeFactory(AbstractThemeFactory):

    __pathToWalkableImage = os.path.join("resources", "images", "map", "mud.png")
    __pathToNotWalkableImage = os.path.join("resources", "images", "map", "wall.png")
    __pathToPlayerImage = os.path.join("resources", "images", "zombie", "zombie.png")

    def __init__(self):
        self.__themeElements = {
            "wt": MapElement(self.__pathToNotWalkableImage, False),
            "ft": MapElement(self.__pathToWalkableImage, True),
            "pl": Player(self.__pathToPlayerImage)
        }

    def createThemeElement(self, elementType):
        return self.__themeElements[elementType]




