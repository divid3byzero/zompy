__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta

class MapElement(BaseTile):
    """
    Base class for map elements
    """
    __metaclass__ = ABCMeta

    def __init__(self, image, walkable):
        """
        Constructor of MapElements
        :param image: image of the element
        :param walkable: specifies whether this element can be accessed by movable objects
        """
        BaseTile.__init__(self, image)
        self.isWalkable = walkable
        self.number = None