__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'

from source.model.worker.FileReader import FileReader


class MapGenerator(object):
    """
    MapGenerator creates a two dimensional list according to the read mapfile.
    This list represents the structure of the map.
    """
    def __init__(self):
        """
        Constructor of the MapGenerator
        :return:
        """
        self.fileReader = FileReader()

    def generateMap(self):
        """
        Generates the two dimensional list representing the map structure
        :return: the two dimensional list
        """
        mapFileContent = self.__createMapArrayFromFile()

        if mapFileContent is not None and len(mapFileContent) > 0:
            mapStructure = []
            for elem in mapFileContent:
                mapRow = elem.strip().split(",")
                mapStructure.append(mapRow)

            return mapStructure

        else:
            raise ValueError("Map is emtpy or cannot be created.")

    def __createMapArrayFromFile(self):
        """
        Returns a list of all lines contained in the mapfile
        :return: the list of lines
        """
        mapFile = self.fileReader.getRandomMapFile()
        return mapFile.read().splitlines()