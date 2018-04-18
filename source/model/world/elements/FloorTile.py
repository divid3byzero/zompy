__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


from model.world.elements.MapElement import MapElement

class FloorTile(MapElement):
    """
    Class representing a walkable floortile of the map
    """

    def __init__(self, image, isSpawnPoint = False):
        """
        Constructor of floor tiles
        :param image: the image of floortiles
        :param isSpawnPoint: optional, specifies whether this tile is a spawnpoint or not
        """
        MapElement.__init__(self, image, True)
        self.isSpawnPoint = isSpawnPoint
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0