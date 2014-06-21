__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

class Pathfinder(object):

    def __init__(self):
        self.startTile = None
        self.endTile = None
        self.map = None
        self.openList = []
        self.closedList = []

    def find(self, zombieTile, playerTile, map):
        self.openList = []
        self.closedList = []
        self.startTile = zombieTile
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
                            self.G(tile, n)
                            self.H(n)
                            self.F(n)
                            self.setParentTile(tile, n)
                    else:
                        self.G(tile, n)
                        self.H(n)
                        self.F(n)
                        self.setParentTile(tile, n)
                        self.openList.append(n)

    def calculate_H(self, tile):
        horizontalDiff = tile.rect.centerx - self.endTile.rect.centerx
        verticalDiff = tile.rect.centery - self.endTile.rect.centery
        h = 10 * (abs(horizontalDiff) + abs(verticalDiff))
        return h

    def G(self, tile, neighborTile):
        neighborTile.g = tile.g + 10

    def H(self, neighbor):
        neighbor.h = self.calculate_H(neighbor)

    def F(self, neighborTile):
        neighborTile.f = neighborTile.h + neighborTile.g

    def setParentTile(self, tile, neighborTile):
        neighborTile.parent = tile