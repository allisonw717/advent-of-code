import helpers
from itertools import combinations
from math import sqrt

helpers.set_file_reader()
f = open('day11.txt') 
lines = f.readlines()

space = [] 
for line in lines:
    space.append([*line.strip()])

#look, i forgot the word for "transpose" so i googled "rotate" instead, oops. 
def flippity_flop(grid):
    flipped_but_tuples = list(zip(*grid[::-1]))
    actual_lists = [] 
    for row in flipped_but_tuples:
        actual_lists.append(list(row))
    return actual_lists

def expand_rows(grid):
    '''
    modifies grid
    '''
    expand_here = [] 
    for i, row in enumerate(grid):
        if row.count(row[0]) == len(row):
            expand_here.append(i)
    for i, row in enumerate(expand_here):
        grid.insert(row + i, ["."] * len(grid[0]))

def find_distance(galaxy_a, galaxy_b):
    x1 = galaxy_a[0]
    x2 = galaxy_b[0]
    y1 = galaxy_a[1]
    y2 = galaxy_b[1]
    return abs(x1-x2) + abs(y1-y2)

def get_galaxy_pairs(space):
    galaxies = []
    for row, line in enumerate(space):
        for col, symbol in enumerate(line):
            if symbol == "#":
                galaxies.append((row,col))
    return list(combinations(galaxies,2))

def part_one():
    expand_rows(space)
    flipped = flippity_flop(space)
    expand_rows(flipped)
    new_space = flippity_flop(flipped)
    keep_flipping = flippity_flop(new_space)
    final_space = flippity_flop(keep_flipping)

    pairs = get_galaxy_pairs(final_space)

    distance_sum = 0
    for pair in pairs:
        distance_sum += find_distance(pair[0], pair[1])

    print(distance_sum)

def get_expanding_indices(grid):
    expand_here = [] 
    for i, row in enumerate(grid):
        if row.count(row[0]) == len(row):
            expand_here.append(i)
    return expand_here

def expansion_counts(galaxy_a, galaxy_b, empty_rows, empty_cols):
    rows = [galaxy_a[0], galaxy_b[0]]
    cols  = [galaxy_a[1], galaxy_b[1]]
    rows.sort()
    cols.sort()
    row_count = 0 
    for row in empty_rows:
        if row in range(rows[0],rows[1]):
            row_count += 1 
    col_count = 0 
    for col in empty_cols:
        if col in range(cols[0], cols[1]):
            col_count += 1
    return (row_count, col_count)

    
def part_two():
    pairs = get_galaxy_pairs(space)
    empty_rows = get_expanding_indices(space)
    empty_cols = get_expanding_indices(flippity_flop(space))
    distance_sum = 0 
    for pair in pairs:
        additional_rows, additional_cols = expansion_counts(pair[0],pair[1],empty_rows,empty_cols)
        distance = find_distance(pair[0],pair[1]) + (additional_rows * 999999) + (additional_cols * 999999)
        distance_sum += distance
    print(distance_sum)


#RUN ONE AT A TIME CUZ I'M USING ONE SPACE LMFAOOOO 
#part_one()
part_two()

#513171773355

