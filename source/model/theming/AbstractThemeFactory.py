__author__ = 'bene'

from abc import ABCMeta, abstractmethod
from source.model.objects.Player import Player
from source.model.world.elements.FloorTile import FloorTile
from source.model.world.elements.WallTile import WallTile

class AbstractThemeFactory(object):
    __metaclass__ = ABCMeta

    themeElements = {
        "wt": "_createWall",
        "ft": "_createFloor",
        "pl": "_createPlayer",
        "sp": "_createSpawnPoint"
    }

    # Only publicly visible access point.
    def createThemeElement(self, elementIndicator):
        creator = self.themeElements[elementIndicator]
        return getattr(self, creator)()

    # Protected methods.
    @abstractmethod
    def _createWall(self):
        pass

    @abstractmethod
    def _createFloor(self):
        pass

    @abstractmethod
    def _createPlayer(self):
        pass

    @abstractmethod
    def _createSpawnPoint(self):
        pass

