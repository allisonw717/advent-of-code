from collections import defaultdict

f = open('2024/input.txt')
input = f.readlines()

class Coord:
    def __init__(self, i,j):
        self.i = i 
        self.j = j 

    def __str__(self):
        return "(" + str(self.i) + ", " + str(self.j) + ")" 
    
    def __eq__(self,other):
        return self.i == other.i and self.j == other.j
    
    #idk tbh
    def __hash__(self):
        return self.i * self.j

    def get_next(self, dir):
        match dir: 
            case "LEFT":
                return Coord(self.i,self.j-1)
            case "RIGHT": 
                return Coord(self.i,self.j+1)
            case "UP": 
                return Coord(self.i-1,self.j)
            case "DOWN": 
                return Coord(self.i+1, self.j)
        
    def in_grid(self, grid):
        if self.i >= 0 and self.i < len(grid[0]) and self.j >= 0 and self.j < len(grid):
            return True
        return False
    

#ummmm don't @ me
class Directions:
    def __init__(self):
        self.dirs = ["UP","RIGHT","DOWN","LEFT"]
        self.index = 0
    def next_dir(self):
        if self.index < 3:
            dir = self.dirs[self.index]
            self.index += 1
            return dir
        else:
            self.index = 0 
            return self.dirs[3]
    
grid = [] 
visited = set() 
for i, line in enumerate(input):
    grid.append(list(line.strip()))
    if "^" in line:
        guard_i, guard_j = i, line.index("^")
        grid[guard_i][guard_j] = "X"

###PART 1
start_pos = Coord(guard_i,guard_j)
curr_pos = start_pos

dirs = Directions()
direction = dirs.next_dir()
in_grid = True

visited = set()
visited.add(curr_pos)
while in_grid: 
    next_pos = curr_pos.get_next(direction)
    if next_pos.in_grid(grid):
        if grid[next_pos.i][next_pos.j] == "#":
            direction = dirs.next_dir()
        else:
            # grid[next_pos.i][next_pos.j] = "X"
            visited.add(next_pos)
            curr_pos = next_pos
    else: 
        in_grid = False
print(len(visited))


###PART 2 
def probably_stuck(list):
    for x in list: 
        if x > 5: 
            return True
    return False


#what in the brute force? 
def is_stuck(start_pos, obsticle, grid):

    curr_pos = start_pos
    grid[obsticle.i][obsticle.j] = "#"

    dirs = Directions()
    direction = dirs.next_dir()
    in_grid = True

    visit_count = defaultdict(int)

    while in_grid: 
        next_pos = curr_pos.get_next(direction)
        if next_pos.in_grid(grid):
            if grid[next_pos.i][next_pos.j] == "#":
                direction = dirs.next_dir()
            else:
                visit_count[next_pos] += 1 
                if probably_stuck(list(visit_count.values())): #LOL
                    grid[obsticle.i][obsticle.j] = "."
                    return True
                curr_pos = next_pos
        else: 
            #lol put it back
            grid[obsticle.i][obsticle.j] = "."
            return False
    return True

count = 0 
for i in range(0,len(grid[0])):
    for j in range(0,len(grid)):
        if grid[i][j] == ".":
            if is_stuck(start_pos, Coord(i,j), grid):
                count += 1 
                print(count)

print(count)
    

    


    

    

