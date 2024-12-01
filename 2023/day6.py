import helpers

helpers.set_file_reader()
f = open('day6.txt') 
lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].strip().split()]
distances = [int(x) for x in lines[1].split(":")[1].strip().split()]

def part_one():
    yeehaw = 1
    for i in range(0,len(times)):
        time = times[i]
        record = distances[i]
        count = 0 
        for button_time in range(1, time):
            move_time = time - button_time
            distance = move_time * button_time
            if distance > record:
                count += 1
        yeehaw *= count
    print(yeehaw)

def part_two():
    time = 51699878
    record = 377117112241505
    count = 0
    for button_time in range(1, time):
        move_time = time - button_time
        distance = move_time * button_time
        if distance > record:
            count += 1
    print(count)

part_two()


