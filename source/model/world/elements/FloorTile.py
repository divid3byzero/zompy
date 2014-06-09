from source.model.world.elements.MapElement import MapElement

__author__ = 'Sebastian'


class FloorTile(MapElement):

    def __init__(self, image):
        MapElement.__init__(self, image, True)