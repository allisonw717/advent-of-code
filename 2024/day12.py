from collections import deque
import itertools

f = open('2024/input.txt')
input = f.readlines()

def in_grid(point):
    if point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0]):
        return True
    return False

def get_all_adj(coord):
    left = (coord[0], coord[1] - 1)
    right = (coord[0], coord[1] + 1)
    up = (coord[0] - 1, coord[1])
    down = (coord[0] + 1, coord[1])
    return [left,right,up,down]

def get_adjacent_plot(grid, coord, value):
    valid_adj = []
    for coord in get_all_adj(coord): 
        if in_grid(coord) and grid[coord[0]][coord[1]] == value:
            valid_adj.append(coord)
    return valid_adj

def get_value(coord):
    return grid[coord[0]][coord[1]]

def bfs(unvisited, root, value):
    q = deque()
    visited = set()
    visited.add(root)
    q.append(root)
    while q:   
        curr = q.popleft()
        for coord in get_adjacent_plot(grid, curr, value):
            if coord not in visited:
                visited.add(coord)
                unvisited.remove(coord)
                q.append(coord)
    return visited

def get_perimeter(plot):
    perimeter = 0 
    for coord in plot: 
        for adj in get_all_adj(coord):
            if not in_grid(adj) or get_value(adj) != get_value(coord):
                perimeter += 1
    return perimeter

def is_corner(coord_a, coord_b):
    try:
        if abs(((coord_a[0] - coord_b[0])) / (coord_a[1] - coord_b[1]) ) == 1:
            return True
        return False
    except:
        return False #lol 

def get_sides(plot):
    corners = 0 
    for coord in plot: 
        sides_on_square = 0
        adj_coords = [] 
        for adj in get_all_adj(coord):
            if not in_grid(adj) or get_value(adj) != get_value(coord):
                sides_on_square += 1
                adj_coords.append(adj)
        if sides_on_square >= 2:
            for pair in itertools.combinations(adj_coords,2):
                if is_corner(pair[0], pair[1]):
                    corners += 1
    return corners


grid = [] 
unvisited = set() 
for i, line in enumerate(input):
    row = list(line.strip())
    for j, val in enumerate(row): 
        unvisited.add((i,j))
    grid.append(row)

total_cost = 0 
discount_cost = 0 
while unvisited:
    root = unvisited.pop()
    plot = bfs(unvisited, root, grid[root[0]][root[1]])
    cost = len(plot) * get_perimeter(plot)
    #discount_cost += len(plot) * get_sides(plot)
    print(get_value(root), get_sides(plot))
    total_cost += cost

print(total_cost)
print(discount_cost)






