__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


class Pathfinder(object):
    """
    The Pathfinder class provides pathfinding (shortest path to the player)
    for enemies by implementing the a*-Algorithm
    """

    def __init__(self):
        """ Constructor of the pathfinder """
        self.startTile = None
        self.endTile = None
        self.map = None
        self.openList = []
        self.closedList = []

    def find(self, enemyTile, playerTile, map):
        """
        Calculates the shortest path and returns the next tile to step on
        :param enemyTile: the current position of the enemy
        :param playerTile: the current position of the player
        :param map: the used map
        :return: the next tile for the enemy to step on
        """
        self.openList = []
        self.closedList = []
        self.startTile = enemyTile
        self.endTile = playerTile
        if not self.map:
            self.map = map

        self.openList.append(self.startTile)

        while len(self.openList):
            tile = self.openList.pop(0)
            self.closedList.append(tile)

            if self.startTile is self.endTile:
                return self.endTile

            if tile is self.endTile:
                t = tile
                while t.parent is not self.startTile and t.parent is not None:
                    t = t.parent
                if t.parent is self.startTile:
                    return t

            for n in map.getNeighbors(tile):
                if n not in self.closedList:
                    if n in self.openList:
                        if n.g > tile.g + 10:
                            self.__G(tile, n)
                            self.__H(n)
                            self.__F(n)
                            self.__setParentTile(tile, n)
                    else:
                        self.__G(tile, n)
                        self.__H(n)
                        self.__F(n)
                        self.__setParentTile(tile, n)
                        self.openList.append(n)

    def __calculate_H(self, tile):
        """
        Calculates the heuristic h-value by using the manhattan distance metric
        :param tile: the current tile
        :return: teh h-value
        """
        horizontalDiff = tile.rect.centerx - self.endTile.rect.centerx
        verticalDiff = tile.rect.centery - self.endTile.rect.centery
        h = 10 * (abs(horizontalDiff) + abs(verticalDiff))
        return h

    def __G(self, tile, neighborTile):
        """
        Calculates the cost of moving to the surrounding tiles
        :param tile: the current tile
        :param neighborTile: the current neighbor tile
        """
        neighborTile.g = tile.g + 10

    def __H(self, neighbor):
        """
        Calculates the h-value for the given neighbor tile
        :param neighbor: the current tile of the surrounding tiles
        """
        neighbor.h = self.__calculate_H(neighbor)

    def __F(self, neighborTile):
        """
        Calculates the f-value by summing up the h and g values
        :param neighborTile: the current neighbor tile
        """
        neighborTile.f = neighborTile.h + neighborTile.g

    def __setParentTile(self, tile, neighborTile):
        """
        Sets the parent tile of the current neighbor
        :param tile: the current tile (the center tile of the neighbor tiles)
        :param neighborTile: the current neighbor tile
        """
        neighborTile.parent = tile