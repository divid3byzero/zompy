__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'



import os
import random
class FileReader(object):
    """
    FileReader class to read map files form the file system
    """
    pathToMaps = os.path.join(os.getcwd(), "resources", "maps")

    def __init__(self):
        """
        Constructor of the FileReader
        """
        pass

    def getRandomMapFile(self):
        """
        Randomly getting an available mapfile
        :return: the file object
        """
        mapFileNames = self.__getMapFileNames()
        return open(mapFileNames[random.randint(0, len(mapFileNames) - 1)])

    def __getMapFileNames(self):
        """
        Getting the filenames of all available mapfiles in the maps directory
        :return: the names of all available maps
        """
        maps = os.listdir(self.pathToMaps)
        mapNames = []
        if os.path.isdir(self.pathToMaps) and len(maps) > 0:
            for mapElem in maps:
                mapNames.append(os.path.join(self.pathToMaps, mapElem))
        else:
            raise ValueError("Cannot open map. No such file or directory.")
        return mapNames