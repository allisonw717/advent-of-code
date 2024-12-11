f = open('2024/input.txt')
input = f.readlines()

def in_grid(point):
    if point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0]):
        return True
    return False

def get_adjacent(coord):
    left = (coord[0], coord[1] - 1)
    right = (coord[0], coord[1] + 1)
    up = (coord[0] - 1, coord[1])
    down = (coord[0] + 1, coord[1])
    adj = [left, right, up, down]
    for coord in adj: 
        if not in_grid(coord):
            adj.remove(coord)
    return adj 

def get_value(coord):
    return grid[coord[0]][coord[1]]

def dfs_ish(curr, visited, path_count):
    value = get_value(curr)
#    if value == 9 and curr not in visited: #part 1
    if value == 9: #part 2 (lol)
        path_count[0] += 1
    visited.add(curr)
    for adj in get_adjacent(curr):
        if get_value(adj) == value + 1:
            dfs_ish(adj, visited, path_count)

grid = [] 
trailheads = [] 
for i, line in enumerate(input):
    row = [int(x) for x in list(line.strip())]
    grid.append(row)
    for j in range(0, len(row)):
        if grid[i][j] == 0:
            trailheads.append((i,j))

total_score = 0 
for trailhead in trailheads:
    path_count = [0]
    visited = set()
    dfs_ish(trailhead, visited, path_count)
    total_score += path_count[0]

print(total_score)

    
