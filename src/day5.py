import helpers

helpers.set_file_reader()
f = open('day5.txt') 
lines = f.readlines()

class farm_range:
    def __init__(self, source_start, dest_start, length):
        self.source_start = source_start
        self.dest_start = dest_start
        self.length = length
    def in_range(self, value):
        if value in range(self.source_start, self.source_start + self.length):
            return True
        return False
    def get_dest(self, source):
        return self.dest_start + (source - self.source_start)
    
class farm_map:
    def __init__(self, name):
        self.ranges = [] 
        self.name = name
    def add_range(self, range):
        self.ranges.append(range)
    def get_value(self, source_number):
        for range in self.ranges:
            if range.in_range(source_number):
                return range.get_dest(source_number)
        return source_number

def part_one():
    seeds = [int(x) for x in lines[0].split(":")[1].split()]
    maps = [] 
    for line in lines[2:]:
        if line in ['\n', '\r\n']:
            maps.append(current_map)
        elif "map" in line:
            current_map = farm_map(line)
        else: 
            range_info = [int(x) for x in line.split()]
            current_map.add_range(farm_range(range_info[1], range_info[0], range_info[2]))
    maps.append(current_map)
    locations = []   
    for seed in seeds:
        for map in maps: 
            seed = map.get_value(seed)
        locations.append(seed)
    print(min(locations))


def get_next_range(ranges, map):
    dests = [] 
    for my_range in ranges:
        for source in map.keys():
            if my_range[0] >= source[0] and my_range[1] <= source[1]:
                dests.append((my_range[0] + map[source], my_range[1] + map[source]))
    return dests


def part_two():
    ranges = []
    seeds = lines[0].split(":")[1].split()
    i = 0 
    while i < len(seeds) - 1:
        ranges.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1))
        i += 2
    print(ranges)
    my_map = {} 
    for line in lines[2:]:
        if line in ['\n', '\r\n']:
            continue
        elif "map" in line:
            print("map yeah")
        else: 
            range_info = [int(x) for x in line.split()]
            my_map[(range_info[1], range_info[1] + range_info[2] - 1)] = range_info[0] - range_info[1]
            
    print(my_map)
    print("sort" + str(sorted(my_map.keys())))
    print(get_next_range(ranges, my_map))

            

part_two()

        


    