__author__ = 'bene'


import os
import random
class FileReader(object):

    pathToMaps = os.path.join("resources", "maps")

    def __init__(self):
        pass

    def getRandomMapFile(self):
        mapFileNames = self.__getMapFileNames()
        return open(mapFileNames[random.randint(0, len(mapFileNames) - 1)])

    def __getMapFileNames(self):

        maps = os.listdir(self.pathToMaps)
        mapNames = []
        if os.path.isdir(self.pathToMaps) and len(maps) > 0:
            for mapElem in maps:
                mapNames.append(os.path.join(self.pathToMaps, mapElem))
        else:
            raise ValueError("Cannot open map. No such file or directory.")
        return mapNames

