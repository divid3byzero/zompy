__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.base.BaseTile import BaseTile
from abc import ABCMeta

class MapElement(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, image, walkable):
            BaseTile.__init__(self, image)
            self.isWalkable = walkable
            self.number = None