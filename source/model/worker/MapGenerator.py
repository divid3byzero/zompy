__author__ = 'Benedikt Buchner (7001697) / Sebastian Hanna (7001788)'


from source.model.worker.FileReader import FileReader
class MapGenerator(object):

    def __init__(self):
        self.fileReader = FileReader()

    def generateMap(self):
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
        mapFile = self.fileReader.getRandomMapFile()
        return mapFile.read().splitlines()