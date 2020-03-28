#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pc
#
# Created:     28/03/2020
# Copyright:   (c) pc 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import copy, random, time

#Fills up the cells randomly in a list of list
def fillingCellsRandomly(height, width):
    nextCells = []
    for x in range(width):
        column = [] # Create a new column.
        for y in range(height):
            if random.randint(0, 1) == 0:
               column.append('#') # Adding a living cell.
            else:
               column.append(' ') # Adding a dead cell.
        nextCells.append(column) # nextCells is a list of column lists.
    return nextCells


def conwayLifeGame(height, width):
    nextCells = []
    nextCells = fillingCellsRandomly(height, width)
    while True:
        print("+++++ New Step +++++\n")
        currentCells = copy.deepcopy(nextCells)

          # Print currentCells on the screen:
        for y in range(height):
            for x in range(width):
                print(currentCells[x][y], end='') # Print the # or space, i.e dead or living cells.
                print() # Print a newline at the end of the row.
         # Calculate the next step's cells based on current step's cells:
        for x in range(width):
            for y in range(height):
                # Get neighboring coordinates:

                leftCoord  = (x - 1) % width
                rightCoord = (x + 1) % width
                aboveCoord = (y - 1) % height
                belowCoord = (y + 1) % height

                # Count number of living neighbors:
                nbNeighbor = 0
                if currentCells[leftCoord][aboveCoord] == '#':
                   nbNeighbor += 1 # Top-left neighbor is alive.
                if currentCells[x][aboveCoord] == '#':
                   nbNeighbor += 1 # Top neighbor is alive.
                if currentCells[rightCoord][aboveCoord] == '#':
                   nbNeighbor += 1 # Top-right neighbor is alive.
                if currentCells[leftCoord][y] == '#':
                   nbNeighbor += 1 # Left neighbor is alive.
                if currentCells[rightCoord][y] == '#':
                   nbNeighbor += 1 # Right neighbor is alive.
                if currentCells[leftCoord][belowCoord] == '#':
                   nbNeighbor += 1 # Bottom-left neighbor is alive.
                if currentCells[x][belowCoord] == '#':
                   nbNeighbor += 1 # Bottom neighbor is alive.
                if currentCells[rightCoord][belowCoord] == '#':
                   nbNeighbor += 1 # Bottom-right neighbor is alive.

                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == '#' and (nbNeighbor == 2 or
nbNeighbor == 3):
                   # Living cells with 2 or 3 neighbors stay alive:
                   nextCells[x][y] = '#'
                elif currentCells[x][y] == ' ' and nbNeighbor == 3:
                    # Dead cells with 3 neighbors become alive:
                    nextCells[x][y] = '#'
                else:
                    # Everything else dies or stays dead:
                    nextCells[x][y] = ' '

        time.sleep(1) # Add a 1-second pause to reduce flickering.



conwayLifeGame(20, 60)

