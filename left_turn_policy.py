# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [2, 0]  # given in the form [row,col]

cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid, init, goal, cost):

    closed = [[[0,0,0,0] if gg==0 else [1,1,1,1] for gg in g] for g in grid]

    x = init[0]
    y = init[1]
    z = init[2]
    g = 0

    open = [[g, x, y, z]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    optimal = False

    cnt = 0
    cache = []
    min_cost = 17


    while not found and not resign and not optimal:

        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            z = next[3]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:

                if all([c for a in closed for b in a for c in b]) == 1: # check

                    optimal = True

                else:

                    for i in range(len(forward)):
                        x2 = x + forward[i][0]
                        y2 = y + forward[i][1]
                        z2 = i

                        if z2 == z:
                            a = 1 # forward
                        elif z2-z in [1, -3]:
                            a = 2 # left
                        else:
                            a = 0 # right


                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):

                            if closed[x2][y2][z2]==0 and grid[x2][y2] == 0:

                                g2 = g + cost[a]
                                old = min(closed[x2][y2])

                                if g2 < old or old == 0:
                                    open.append([g2, x2, y2, z2])
                                print([g2, x2, y2, z2])
                                closed[x2][y2][z2] = 1

                                # save path.
                                landed = [x, y, z, x2, y2, z2, a, action_name[a]]
                                cache.append(landed)

    path = []
    dest = init
    print(cache)

    while dest != goal+[2]:
        for k in cache:
            if k[:3] == dest:
                path.append(k)
                dest = k[3:6]
    # print(path)

    expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    expand[goal[0]][goal[1]] = '*'
    for p in path:
        expand[p[0]][p[1]] = p[7]

    policy2D = expand
    return policy2D

p = optimum_policy2D(grid, init, goal, cost)
for i in p:
    print(i)