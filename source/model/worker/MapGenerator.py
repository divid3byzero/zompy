__author__ = 'bene'

from source.model.worker.FileReader import FileReader
class MapGenerator(object):

    def __init__(self):
        self.fileReader = FileReader()

    def generateMap(self):
        mapFileContent = self.__createMapArrayFromFile()

        if mapFileContent is not None and len(mapFileContent) > 0:
            mapStructure = []
            for elem in mapFileContent:

                tempRow = elem.strip().split(",")

                mapRow = []
                for stringCoordinate in tempRow:
                    mapRow.append(int(stringCoordinate))

                mapStructure.append(mapRow)

            return mapStructure

        else:
            raise ValueError("Map is emtpy or cannot be created.ss")

    def __createMapArrayFromFile(self):
        mapFile = self.fileReader.getRandomMapFile()
        return mapFile.read().splitlines()