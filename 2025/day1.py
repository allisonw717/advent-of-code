
f = open('2025/input.txt') 
lines = [line.strip() for line in f.readlines()]

dial = 50 
count_zero = 0 

#part 1 
for line in lines:
    operator = line[0]
    number = int(line[1:])
    if operator == "L":
        dial = (dial - number) % 100 #suspicious working but why
    else:
        dial = (dial + number) % 100
    if dial == 0:
        count_zero += 1

print(count_zero)

dial = 50 
count_zero = 0 

#part 2, really bad
for line in lines:
    operator = line[0]
    number = int(line[1:])
    if operator == "R":
        count_zero += (dial + number) // 100 
        dial = (dial + number) % 100 
    else:
        if dial - number <= 0: 
            count_zero += ((number - dial) // 100) + 1
            if dial == 0: 
                count_zero -= 1 
        dial = (dial - number) % 100

    print(line, dial)
    print(count_zero)



