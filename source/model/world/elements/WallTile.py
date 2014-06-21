__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.world.elements.MapElement import MapElement

class WallTile(MapElement):

    def __init__(self, image):
        MapElement.__init__(self, image, False)