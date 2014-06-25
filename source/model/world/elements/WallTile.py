__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.world.elements.MapElement import MapElement

class WallTile(MapElement):
    """
    Class representing a non-walkable walltile of the map
    """
    def __init__(self, image):
        """
        Conctrsuctor of walltiles
        :param image: image of the walltiles
        """
        MapElement.__init__(self, image, False)