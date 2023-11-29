import helpers

"""
Day 1 of 2022 to remember how to code lmfao 
"""

helpers.set_file_reader()
f = open('day0.txt') 
lines = f.readlines()

#PART 1
max_elf_weight = 0
elf_weight = 0 
for line in lines:
    if line != "\n":
        elf_weight += int(line.strip())
    else:
        if elf_weight > max_elf_weight:
            max_elf_weight = elf_weight
        elf_weight = 0 
    
print(max_elf_weight)

#PART 2
elf_weights = [] 
elf_weight = 0 
for line in lines:
    if line != "\n":
        elf_weight += int(line.strip())
    else:
        elf_weights.append(elf_weight)
        elf_weight = 0 
elf_weights.sort()
print(sum(elf_weights[-3:]))