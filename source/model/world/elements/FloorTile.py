from source.model.world.elements.MapElement import MapElement

__author__ = 'Sebastian'


class FloorTile(MapElement):

    def __init__(self, image, isSpawnPoint = False):
        MapElement.__init__(self, image, True)
        self.isSpawnPoint = isSpawnPoint
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0