import helpers
import math

helpers.set_file_reader()
f = open('day8.txt') 
lines = f.readlines()

class steps:
    def __init__(self, steps):
        self.steps = steps
        self.length = len(self.steps)
        self.index = -1 
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == self.length:
            self.index = 0 
        if self.steps[self.index] == 'L':
            return 0 
        return 1
    



map = {}
starts = [] 
for line in lines[2:]:
    key, values = line.split("=")
    if(key[2] == 'A'):
        starts.append(key.strip())
    map[key.strip()] = (values[2:5], values[7:10])

def part_one():   
    steps_iter = steps(lines[0].strip())
    count = 0 
    curr = 'AAA'
    next_string = ''
    while curr != 'ZZZ':
        next_string = map[curr][next(steps_iter)]
        curr = next_string
        count += 1
    print(count)

def get_count(start):
    count = 0 
    steps_iter = steps(lines[0].strip())
    curr = start 
    next_string = ''
    while curr[2] != 'Z':
        next_string = map[curr][next(steps_iter)]
        curr = next_string
        count += 1
    return count 

def part_two():
    counts = [] 
    for start in starts:
        counts.append(get_count(start))
    return(math.lcm(*counts))

print(part_two())








        
