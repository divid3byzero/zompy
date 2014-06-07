__author__ = 'bene'

import unittest
from source.model.worker.MapGenerator import MapGenerator
class AppTestSuite(unittest.TestCase):

    pathToTestMapFile = "../source/resources/test.map"

    def testCreateMapFromFile(self):
        mapGenerator = MapGenerator(self.pathToTestMapFile)
        generatedMap = mapGenerator.generateMap()
        self.assertIsNotNone(generatedMap)
        self.assertGreater(len(generatedMap), 0)


    def testMapCoordinateType(self):
        mapGenerator = MapGenerator(self.pathToTestMapFile)
        generatedMap = mapGenerator.generateMap()

        for elem in generatedMap:

            for coordinate in elem:
                self.assertTrue(type(coordinate) == int)
                print type(coordinate)

if __name__ == "__main__":
    suite = unittest.TestLoader.loadTestsFromTestCase(AppTestSuite)
    unittest.TextTestRunner(verbosity=2).run(suite)
