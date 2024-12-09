from collections import defaultdict
import itertools

f = open('2024/input.txt')
input = f.readlines()

def subtract(point_a, point_b):
    return (point_a[0] - point_b[0]),(point_a[1] - point_b[1])

def in_grid(point):
    if point[0] >= 0 and point[0] < len(grid) and point[1] >= 0 and point[1] < len(grid[0]):
        return True
    return False

grid = [] 
antennas = defaultdict(list)
for i, line in enumerate(input):
    row = list(line.strip())
    grid.append(row)
    for j in range(0, len(row)):
        if grid[i][j] != ".":
            antennas[grid[i][j]].append((i,j))

#PART 1 
antinodes = set()
for antenna, locations in antennas.items():
    for pair in itertools.combinations(locations,2): #nice
        diff1 = subtract(pair[0], pair[1])
        diff2 = subtract(pair[1], pair[0])
        antinode1 = subtract(pair[1],diff1)
        antinode2 = subtract(pair[0],diff2)
        if in_grid(antinode1):
            antinodes.add(antinode1)
        if in_grid(antinode2):
            antinodes.add(antinode2)

print(len(antinodes))

#PART 2 change it up just a bit
def add_nodes_b_side(point_a, point_b, nodes):
    diff = subtract(point_a, point_b)
    node = subtract(point_b, diff)
    while in_grid(node):
        nodes.add(node)
        grid[node[0]][node[1]] = "#"
        next_node = subtract(node,diff)
        node = next_node

antinodes = set()
for antenna, locations in antennas.items():
    for pair in itertools.combinations(locations,2): #nice
        antinodes.add(pair[0])
        antinodes.add(pair[1])
        add_nodes_b_side(pair[0], pair[1], antinodes)
        add_nodes_b_side(pair[1], pair[0], antinodes)

print(len(antinodes))

# for i, line in enumerate(grid):
#     print(''.join(line))
