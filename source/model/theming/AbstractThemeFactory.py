__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


from abc import ABCMeta, abstractmethod
from model.objects.Player import Player
from model.world.elements.FloorTile import FloorTile
from model.world.elements.WallTile import WallTile

class AbstractThemeFactory(object):
    """
    Abstract factory class for all theming factories
    """
    __metaclass__ = ABCMeta

    themeElements = {
        "wt": "_createWall",
        "ft": "_createFloor",
        "pl": "_createPlayer",
        "sp": "_createSpawnPoint"
    }

    def createThemeElement(self, elementIndicator):
        """
        Creates the tile according to the passed elementIndicator
        :param elementIndicator: the indicator for the tile to be created
        :return: the tile
        """
        creator = self.themeElements[elementIndicator]
        return getattr(self, creator)()

    @abstractmethod
    def _createWall(self):
        """
        Abstract method for creating wall-tiles. Has to be implemented by concrete factories.
        """
        pass

    @abstractmethod
    def _createFloor(self):
        """
        Abstract method for creating floor-tiles. Has to be implemented by concrete factories.
        """
        pass

    @abstractmethod
    def _createPlayer(self):
        """
        Abstract method for creating player-objects. Has to be implemented by concrete factories.
        """
        pass

    @abstractmethod
    def _createSpawnPoint(self):
        """
        Abstract method for creating spawnpoint-tiles. Has to be implemented by concrete factories.
        """
        pass

