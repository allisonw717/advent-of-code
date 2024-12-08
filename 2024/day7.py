import itertools

f = open('2024/input.txt')
input = f.readlines()

equations = {} 
for line in input:
    value_str, nums_str = line.strip().split(": ")
    equations[int(value_str)] = [int(x) for x in nums_str.split(" ")]

def do_the_math(a, b, operation):
    if operation == "*":
        return a * b
    elif operation == "+":
        return a + b
    elif operation == "||":
        return int(str(a)+str(b))
    
def get_possible_results(nums):
    results = [] 
    operator_count = len(nums) - 1
    operators = ["*","+","||"]
    for operation in itertools.product(operators, repeat=operator_count):
        result = nums[0]
        for i in range(1,len(nums)):
            result = do_the_math(result, nums[i],operation[i-1])
        results.append(result)
    return results
    
sum = 0 
for a,b in equations.items():
    results = get_possible_results(b)
    if a in results:
        sum += a

print(sum)

        






