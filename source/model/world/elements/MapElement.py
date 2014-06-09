from source.model.base.BaseTile import BaseTile
from abc import ABCMeta

__author__ = 'Sebastian'


class MapElement(BaseTile):
    __metaclass__ = ABCMeta

    def __init__(self, image, walkable):
            BaseTile.__init__(self, image)
            self.isWalkable = walkable