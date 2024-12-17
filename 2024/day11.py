from collections import defaultdict

f = open('2024/input.txt')
input = f.readlines()

for line in input:
    stones = [int(x) for x in list(line.strip().split())]
    

def blink(stones):
    index = 0 
    start_length = len(stones)
    while index < start_length:
        num = stones[index]
        if num == 0:
            stones[index] = 1
        elif len(str(num)) % 2 == 0: 
            length = len(str(num))
            stones[index] = int(str(num)[:int(length/2)])
            stones.append(int(str(num)[int(length/2):]))
        else:
            stones[index] = stones[index] * 2024
        index += 1
    return stones

def get_stone_dict(stones):
    stone_count = defaultdict(int)
    for stone in stones:
        stone_count[stone] += 1 
    return stone_count

def blink_faster(stone_dict):
    additions = defaultdict(int)
    for stone, count in stone_dict.items():
        if stone == 0:
            additions[1] += count 
        elif len(str(stone)) % 2 == 0: 
            length = len(str(stone))
            additions[int(str(stone)[:int(length/2)])] += count 
            additions[int(str(stone)[int(length/2):])] += count 
        else:
            additions[stone * 2024] += count 
    return additions



# for i in range(1,26):
#     print(i)
#     stones = blink(stones)

# print(len(stones))
        
stone_dict = get_stone_dict(stones)
for i in range(1,76):
    stone_dict = blink_faster(stone_dict)

print(sum(stone_dict.values()))

