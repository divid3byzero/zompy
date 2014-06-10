__author__ = 'Sebastian'

import pygame

def aStar(startNode, targetNode, map):

    # searching all valid neighbors and setting the start node as predecessor
    def getAdjacentNodes(startNode):
        adjacentNumbers = { # calculating the numbers of all adjacent nodes
            "N" : startNode.number - map.amountHorizontal, # north
            "NE" : startNode.number - map.amountHorizontal + 1, # north east
            "E" : startNode.number + 1, # east
            "SE" : startNode.number + map.amountHorizontal + 1, # south east
            "S" : startNode.number + map.amountHorizontal, # south
            "SW" : startNode.number + map.amountHorizontal - 1, # south west
            "W" : startNode.number - 1, # west
            "NW" : startNode.number - map.amountHorizontal - 1 # north west
        }

        adjacents = {}
        for k, v in adjacentNumbers.iteritems():
            node = map.getTileByNumber(v) # getting the node for each number
            if node.isWalkable and node not in closedList:
                node.predecessor = startNode
                adjacents.update({k : node})
        return adjacents


    # calculate F, G, H
    def calculateValues(node, targetNode):
        # H is calculated using the manhattan method
        node.H = abs(node.rect.x - targetNode.rect.x) + abs(node.rect.y - targetNode.rect.y)

        # setting the costs for each step, depending on whether its diagonal or not
        if abs(node.number - node.predecessor.number) in (1, 10):
            node.G = node.predecessor.G + 10
        else:
            node.G = node.predecessor.G + 14

        node.F = node.G + node.H

    # all considerable nodes
    openList = []
    # all checked nodes
    closedList = []

    # adding start node to the open list to process it
    openList.append(startNode)
    # getting all valid adjacent nodes of the start node
    adjacentNodes = getAdjacentNodes(startNode)
    # calculating F, G and H for each valid surrounding node
    # and appending them to the list of not-yet-processed nodes
    for k, node in adjacentNodes.iteritems():
        calculateValues(node, targetNode)
        print("Number: {0}, Direction: {1}, G: {2}, H: {3}, F: {4}".format(node.number, k, node.G, node.H, node.F))
        openList.append(node)
    # remove the start node from the openlist and append it
    # to the closed list (because it has been processed now)
    openList.remove(startNode)
    closedList.append(startNode)
