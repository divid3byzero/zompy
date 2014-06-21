__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

class ViewingDirection(object):

    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"

    @staticmethod
    def getViewingDirections():
        return [ViewingDirection.NORTH, ViewingDirection.EAST, ViewingDirection.SOUTH, ViewingDirection.WEST]

    def __init__(self):
        pass
