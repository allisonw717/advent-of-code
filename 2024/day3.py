import re 

f = open('2024/input.txt')
input = f.readlines()

#part 1 rememeber how to regex 
def getSum(input):
    matches = re.findall(r"mul\(\d+,\d+\)", str(input))
    sum = 0  
    for match in matches:
        a, b = re.findall(r"\d+", match)
        sum += int(a)*int(b)
    return sum 

print(getSum(input))

#part 2 no brain 
total_sum = 0 
parts = str(input).split("do()")
for part in parts:
    if "don\'t()" in part: 
        disabled_start = part.find("don\'t()")
        enabled = part[0:disabled_start]
        total_sum += getSum(enabled)
    else: 
        total_sum += getSum(part)

print(total_sum)