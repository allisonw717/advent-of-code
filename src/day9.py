import helpers

helpers.set_file_reader()
f = open('day9.txt') 
lines = f.readlines()

#why tf am i doing recursion I hate recursion 
#I HAVE NO IDEA HOW THIS WORKS LMFAO 
def get_next(nums):
    if nums[0] == 0 and len(set(nums)) == 1: 
        return 0 
    next_list = [] 
    for i in range(len(nums) - 1,0, -1):
        next_list.insert(0, nums[i] - nums[i-1])
    return nums[-1] + get_next(next_list)

def get_first(nums):
    if nums[0] == 0 and len(set(nums)) == 1: 
        return 0 
    next_list = [] 
    for i in range(len(nums) - 1,0, -1):
        next_list.insert(0, nums[i] - nums[i-1])
    return nums[0] - get_first(next_list) 

sum = 0 
part_two_sum = 0 
for line in lines:
    nums = [int(x) for x in line.split()]
    sum += get_next(nums)
    part_two_sum += get_first(nums)
print(sum)
print(part_two_sum)
