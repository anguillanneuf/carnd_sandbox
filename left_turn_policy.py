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
        [0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right

goal = [3, 0]  # given in the form [row,col]

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
	z = init[2] # orientation / direction
	g = 0
	open = [[g, x, y, z]]
	found = False  # flag that is set when search is complete
	resign = False  # flag set if we can't find expand

	

	cache = []
	while not found and not resign: 
		
		if len(open) == 0:
			resign = True
			return 'fail'
			
#		elif all([c for a in closed for b in a for c in b]) == 1:
#			exhausted = True
			
		else:

			open.sort()
			open.reverse()
			next = open.pop()
			
			x = next[1]
			y = next[2]
			z = next[3]
			g = next[0]
			
#			print("looking at {} from {}".format(next, open_))
			
			if x==goal[0] and y==goal[1]:
#				print("found")
				found = True
			else:
				found = False
				
				for i in range(len(forward)):
					
					x2 = x + forward[i][0]
					y2 = y + forward[i][1]
					z2 = i
					
					if z2 - z in [1, -3]:
						a = 2 # left
					elif z2 - z in [-1, 3]:
						a = 0 # right
					elif z2 == z:
						a = 1 # straight
					else:
						continue # impossible move
					
					g2 = g + cost[a]
					
					if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
						if (closed[x2][y2][z2] == 0 or closed[x2][y2][z2] > g2) and grid[x2][y2] == 0:
#							print("[{},{},{}] to [{},{},{}] can be done".format(x,y,z,x2,y2,z2))
							open.append([g2, x2, y2, z2])
							closed[x2][y2][z2] = g2
							landed = [g, x, y, z, action_name[a], g2, x2, y2, z2]
#							print(landed)
							cache.append(landed)
#							print("\n")
	
#	print("out of while loop")
#	print(cache)
	
	path = []
	dest = min([c[5:] for c in cache if c[6:8]==goal])						
#	print(dest)
	curr = [0]+init
#	print(curr)
	
	while dest != curr:
		for k in cache:
			if k[5:] == dest:
				path.append(k)
				dest = k[:4]

	expand = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
	expand[goal[0]][goal[1]] = '*'
	
#	print(path)
	for p in path:
		expand[p[1]][p[2]] = p[4]
	policy2D = expand
	
	return policy2D
	
p = optimum_policy2D(grid, init, goal, cost)
for i in p:
    print(i)