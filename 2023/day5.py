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


def get_overlap(x, y):
    left = max(x[0], y[0])
    right = min(x[1], y[1])
    if left <= right:
        return (left,right)
    return None

def test_get_overlap():
    print(get_overlap((0,10), (0,0)))
    print(get_overlap((0,10), (5,15)))
    print(get_overlap((5,15), (0,10)))
    print(get_overlap((1,5), (2,3)))
    print(get_overlap((2,3), (1,5)))

def get_next_range(range, map):
    '''
    range = original range
    map = k: ranges that change, v: how much it changes
    returns list of new range applying changes where needed
    '''
    result = [] 
    overlaps = [] 
    for source in map.keys():
        overlap = get_overlap(range, source)
        if overlap:
            overlaps.append(overlap)
            result.append((overlap[0] + map[source], overlap[1] + map[source]))
    if not overlaps:
        return [range] 
    sorted_overlaps = sorted(overlaps)
    for i, overlap in enumerate(sorted_overlaps[:-1]):
        after_end = overlap[1] + 1
        before_next_start = sorted_overlaps[i+1][0] - 1
        if after_end <= before_next_start:
            result.append((after_end, before_next_start))
    if range[0] < sorted_overlaps[0][0]:
        result.append((range[0],sorted_overlaps[0][0] - 1))
    if range[1] > sorted_overlaps[-1][1]:
        result.append((sorted_overlaps[-1][1] + 1, range[1]))
    
    return result 
        
def part_two():
    ranges = []
    seeds = lines[0].split(":")[1].split()
    i = 0 
    while i < len(seeds) - 1:
        ranges.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1))
        i += 2
    for line in lines[2:]:
        if line in ['\n', '\r\n']:
            new_ranges = []
            for range in ranges:
                new_ranges.extend(get_next_range(range, my_map))
            ranges = new_ranges
        elif "map" in line:
            my_map = {} 
        else: 
            range_info = [int(x) for x in line.split()]
            my_map[(range_info[1], range_info[1] + range_info[2] - 1)] = range_info[0] - range_info[1]

    #I don't know why it wasn't processing the last one lol 
    new_ranges = []
    for range in ranges:
        new_ranges.extend(get_next_range(range, my_map))
    ranges = new_ranges

    minimum = min(ranges)
    print("PART TWO ANSWER: " + str(minimum[0]))
            
#test_get_overlap()
part_one()
part_two()
#391544129 is too high 
#13606986 is too high 

        


    