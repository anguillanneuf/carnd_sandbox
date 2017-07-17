# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
# grid = [[0,1],
#         [0,0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------

    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    value = [[99 if gg == 1 else gg for gg in g] for g in grid]
    grid[goal[0]][goal[1]] = 1
    resign = False

    x = goal[0]
    y = goal[1]
    g = 0

    open = [[g, x, y]]
    temp = [y for x in value for y in x]
    temp.pop(goal[0] * len(grid[0]) + goal[1])

    while(not resign and all(temp) == 0):

        if len(open) == 0:
            resign = True

        else:
            for next in [o for o in open if o[0] == min(open)[0]]:

                x = next[1]
                y = next[2]
                g = next[0]

                value[x][y] = g

                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):

                        if grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            grid[x2][y2] = 1

                open.remove(next)

        temp = [y for x in value for y in x]
        temp.pop(goal[0] * len(grid[0]) + goal[1])

    value = [[99 if k==0 else k for k in v] for v in value]
    value[goal[0]][goal[1]]=0
    return value

v = compute_value(grid, goal, cost)

for i in v:
    print(i)