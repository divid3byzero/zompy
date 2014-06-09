__author__ = 'Sebastian'

import pygame

def aStar(startNumber, targetNumber, map):


    def getAdjacentNodes(startNumber):
        adjacentNumbers = { # calculating the numbers of all adjacent nodes
            "N" : startNumber - map.amountHorizontal, # north
            "NE" : startNumber - map.amountHorizontal + 1, # north east
            "E" : startNumber + 1, # east
            "SE" : startNumber + map.amountHorizontal + 1, # south east
            "S" : startNumber + map.amountHorizontal, # south
            "SW" : startNumber + map.amountHorizontal - 1, # south west
            "W" : startNumber - 1, # west
            "NW" : startNumber - map.amountHorizontal - 1 # north west
        }

        adjacents = {}
        for k, v in adjacentNumbers.iteritems():
            node = map.tiles[v] # getting the node for each number
            if node.isWalkable and node not in closedList:
                adjacents.update({k : node})
        return adjacents


    # calculate F, G, H
    def calculateValues(node):
        pass


    openList = [] # all considerable nodes
    closedList = [] # all checked nodes
    parentNode = map.tiles[startNumber] # start node

    openList.append(parentNode) # adding start node to the open list to process it
    adjacentNodes = getAdjacentNodes(startNumber) # getting all valid adjacent nodes of the start node

    # setting the parent node of the adjacent nodes
    for node in adjacentNodes.values():
        node.predecessor = parentNode
        openList.append(node)