import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""A framework for creating instances of Conway's Game of life"""

####                   Tool Box                    ####
########################################################
#               ~~show the plot~~
#       plt.imshow(x, interpolation='nearest')
#       plt.show()
#
#             ~~boundary conditions~~
#     check right = grid[i, (j+1)%N] where N = j
#     check bottom = grid[(i+1)%N, j] where N = i
########################################################


def createGrid(M, N):
    brd = (M, N)
    grid = np.random.choice([0, 255], brd, p=[0.2, 0.8])
    return grid

def zeros(M, N):
    brd = (M, N)
    grid = np.zeros(brd, dtype=int)
    return grid

def addGlider(i, j, grid):
    """add a glider with top left at i, j"""
    glider = np.array([[0,255,0],
                       [0,0,255],
                       [255,255,255]])
    # when using np's slice we must remember that gliders are 3x3 objects
    grid[i:i+3, j:j+3] = glider
    return grid

def applyRules(i, j, N, grid):
    """Apply the rules to conways game to cell (i,j)"""
    total = (grid[i, (j+1)%N] + \
             grid[i, (j-1)%N] + \
             grid[(i-1)%N, j] + \
             grid[(i+1)%N, j] + \
             grid[(i-1)%N, (j-1)%N] + \
             grid[(i-1)%N, (j+1)%N] + \
             grid[(i+1)%N, (j-1)%N] + \
             grid[(i+1)%N, (j+1)%N])
    neighbors = int(total/255)

    # if the cell is alive we have to perform these checks
    if grid[i, j] == 255:
        if (neighbors < 2) or (neighbors > 3):
            return 0
        else:
            return 255
    if grid[i, j] == 0:
        if (neighbors == 3):
            return 255
        else:
            return 0

def updateFunc(frameNum, game, N, grid, applyRules=applyRules):
    """This is the function thats called each fram to update the game of life"""
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            new_grid[i, j] = applyRules(i, j, N, grid)
    grid[:] = new_grid[:]
    return game.set_data(new_grid)

def animate_matplot(N, grid, updateInt, updateFunc=updateFunc):
    """this is the function used to animate the matplot"""
    fig, ax = plt.subplots()
    game = ax.imshow(grid, interpolation="nearest")
    sim = animation.FuncAnimation(fig,
                                  updateFunc,
                                  fargs=(game, N, grid),
                                  frames=1,
                                  interval=updateInt)
    plt.show()
