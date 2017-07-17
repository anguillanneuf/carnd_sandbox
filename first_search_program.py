# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

# grid = [[0, 1],
#         [0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    # optimal path length
    opt = 0

    # positions to be considered by each iteration
    pos = [[opt, 0, 0]]

    # check off init position
    grid[init[0]][init[1]] = 1


    def update(pos, grid):

        # x is the position of interest
        x = sorted(pos)[0]

        # save a copy of this position
        path = x

        # use this position as current position
        curr = x[1:]

        # check off this position
        grid[x[1]][x[2]] = int(1)

        for d in delta:

            # updated current position
            curr[0] = x[1] + d[0]
            curr[1] = x[2] + d[1]

            # if new position is inside the grid and it's not checked off
            # add new position to my list of positions with the cost increased by one unit

            if (curr[0] > -1 and curr[1] > -1 and
                curr[0] < len(grid) and curr[1] < len(grid[0]) and
                grid[curr[0]][curr[1]] != 1):

                pos.append([x[0]+cost]+curr)

        # remove the position that has been looked at
        pos.remove(x)

        return pos, grid, path


    while(len(pos)>0):

        pos, grid, path = update(pos, grid)

        # if the goal isn't in the path after exhausting the search, search has failed
        if(goal != path[1:]):
            path = 'fail'

    return path

path = search(grid, init, goal, cost)
print(path)