# -*- coding: utf-8 -*-
import numpy as np
import random
from copy import copy, deepcopy
"""
Created on Mon Sep 20 14:24:00 2021

@author: Manuel Cruz
"""

def setBoard():
#creates 8x8 array of zeros
    grid = np.zeros((8,8))
    
#places 1 queen in a random row at each column
    for x in range(0, 8):
        random_number = random.randint(0,7)
        grid[random_number][x] = 1
    return grid

def findQueens(array):
    coordinates = []
    for x in range(0,8):
        for y in range(0,8):
            if array[x][y] == 1:
                coordinates.append([x,y])
    return coordinates

def findDiagonals(coords):
    conflicts = 0
    for i in range(0,8):
        for j in range(0,8):
            if i !=j:
                slope = (coords[j][0]-coords[i][0])/(coords[j][1]-coords[i][1])
                if slope == 1 or slope == -1:
                    conflicts = conflicts + 1
    conflicts = conflicts/2
    return conflicts
    
def findHorizontals(coords):
    conflicts = 0
    row = []
    for i in range(0,8):       
#isolate the row values
        row.append(coords[i][0])
    for i in range (0,8):
        if i <=6 and row[i] == row [i+1]:
            conflicts = conflicts + 1
    return conflicts

def findConflicts(coords):
    horizontals = findHorizontals(coords)
    diagonals = findDiagonals(coords)
    result = horizontals + diagonals
    return result

def findNeighbors(coords):
    print('Old queen positions:',coords)
    neighbors = 0
    minimum = deepcopy(findConflicts(coords))
    initialConflicts = deepcopy(findConflicts(coords))
    tempList = deepcopy(coords)
    bestMove = 0
    bestMoveIndex = 0
    tempIndex = 0;
    for i in range(0,8):
        for j in range(0,8):
            coords[i][0]=j
            newConflicts = findConflicts(coords)
            if newConflicts < initialConflicts:
                neighbors = neighbors + 1
                if newConflicts < minimum:
                    minimum = newConflicts
                    bestMove = deepcopy(coords[i])
                    bestMoveIndex = coords.index(bestMove)
                    print('Index: ',bestMoveIndex)
            if coords[i][0] == 7:
                coords[i][0] = tempList[tempIndex][0]
                tempIndex = tempIndex+1
    coords[bestMoveIndex] = bestMove
    print('New queen positions:',coords)
    print('Neighbors: ',neighbors)
    print('minimum: ', minimum)
    print('Best Move: ', bestMove)
    return coords
    

'''
HILL CLIMBING
Only 1 queen gets moved per iteration. move each queen down the column 
that it's in. Then, calculate the heuristic after the change. The one queen
that causes the biggest decrease in heuristic value gets chosen to be moved
and creates the next state.

Using a loop, we will move each queen to the other empty spaces in its column.
Then, calculate both horizontal and diagonal conflicts as a result of the change.
If the heuristic value is lower than that of the current state, it becomes the new minimum.
Repeat process until finally the lowest minimum is recorded.

save coordinates for the queen that will cause the biggest decrease in heuristic value.
move queen to said coordinates and repeat previous steps until solution is found.

'''
board = setBoard()

coords = findQueens(board)
print('Current h: ',(findConflicts(coords)))
print('Current State')
print(board)
coords = findNeighbors(coords)
print(coords)