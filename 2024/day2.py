#f = open('2024/example.txt') 
f = open('2024/input.txt')
lines = f.readlines()

def is_safe(nums):
    increasing = False
    if nums[1] - nums[0] >= 1:
        increasing = True 
    for i in range(0, len(nums)-1):
        diff = nums[i+1] - nums[i]
        if increasing:
            if diff < 1 or diff > 3: 
                return False
            if i == len(nums) - 2: 
                return True
        else:
            if diff < -3 or diff > -1:
                return False
            if i == len(nums) - 2: 
                return True

unsafe = 0 
safe = 0 
og_safe = 0
for line in lines:
    nums = [int(x) for x in line.strip().split()]
    if is_safe(nums):
        safe += 1
        og_safe += 1
    else: 
        unsafe += 1
        print("original:", nums)
        for i in range(0,len(nums)):
            list_copy = list(nums)
            list_copy.pop(i)
            print(list_copy)
            if is_safe(list_copy):
                print("SAFE")
                safe += 1
                break 
    print("----")

print("safe", safe)
print("og safe", og_safe)
print("unsafe",unsafe)
print("total  " + str(len(lines)))

    




    



