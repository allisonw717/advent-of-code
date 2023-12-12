import helpers

helpers.set_file_reader()
f = open('day10.txt') 
lines = f.readlines()

class coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def __add__(self, other):
        return coord(self.row + other.row, self.col + other.col)
    def __eq__(self, other):
        if self.row == other.row and self.col == other.col:
            return True
        return False
    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"

moves = {
    "|" : [coord(-1,0), coord(1,0)],
    "-" : [coord(0,-1), coord(0,1)], 
    "L" : [coord(-1,0), coord(0,1)], 
    "J" : [coord(-1,0), coord(0,-1)],
    "7" : [coord(0,-1), coord(1,0)],
    "F" : [coord(0,1), coord(1,0)]
}

def get_next(prev, curr, symbol):
    where_can_i_go = moves[symbol]
    if prev == curr + where_can_i_go[0]:
        return curr + where_can_i_go[1]
    return curr + where_can_i_go[0]

grid = []
row_num = 0 
for line in lines:
    row = [*line.strip()]
    grid.append(row)
    for i, pipe in enumerate(row):
        if pipe == 'S':
            start = coord(row_num, i)
    row_num += 1

path_one = [start]
path_two = [start] 

second_maybe = [start + coord(-1,0), start + coord(0,-1), start + coord(0,1), start + coord(1,0)]
seconds_not_maybe = [] 
#need to check if second can go back to first bc maybe not 
#I am aware that this is illegible but I knew what was happening when i wrote it
for second_pipe in second_maybe:
    symbol = grid[second_pipe.row][second_pipe.col]
    if symbol != ".":
        for move in moves[symbol]:
            if second_pipe + move == start: 
                seconds_not_maybe.append(second_pipe)

path_one.append(seconds_not_maybe[0])
path_two.append(seconds_not_maybe[1])

steps = 1
while path_one[steps] != path_two[steps]:
    path_one_curr = path_one[steps]
    path_two_curr = path_two[steps]
    path_one.append(get_next(path_one[steps - 1], path_one[steps], grid[path_one_curr.row][path_one_curr.col]))
    path_two.append(get_next(path_two[steps - 1], path_two[steps], grid[path_two_curr.row][path_two_curr.col]))
    steps += 1

print(steps)
#oh shi its actually just bfs why did i do this lol 



