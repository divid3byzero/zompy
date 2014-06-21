__author__ = 'bene'

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
