from source.model.world.elements.MapElement import MapElement

__author__ = 'Sebastian'


class FloorTile(MapElement):

    def __init__(self, image):
        MapElement.__init__(self, image, True)
        self.predecessor = None
        self.G = 0
        self.H = 0
        self.F = 0