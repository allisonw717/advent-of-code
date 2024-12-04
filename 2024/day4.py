import numpy as np 

f = open('2024/input.txt')
input = f.readlines()
height = len(input)

def count_rows(rows):
    count = 0 
    for line in rows:
        count += line.count("XMAS")
        count += line[::-1].count("XMAS")
    return count 

def transpose_but_strings(rows):
    matrix = [] 
    for row in rows:
        matrix.append(list(row.strip()))
    
    input_matrix = np.array(matrix)
    transposed_matrix = np.transpose(input_matrix)

    result = [] 
    for char_line in transposed_matrix:
        string_line = ''.join(char_line)
        result.append(string_line)

    return result

def count_cols(rows):
    cols = transpose_but_strings(rows)
    return count_rows(cols)

count = 0 
count += count_rows(input)
count += count_cols(input)

#no diagonal traversing plz 
input_gonna_be_diagonal = [] 
space_count = 0 
for line in input:
    line = space_count*"-" + line.strip() + (height-space_count)*"-"
    input_gonna_be_diagonal.append(line)
    space_count += 1

count += count_cols(input_gonna_be_diagonal)

# #the other diagonal?? T-T 
other_diagonal = [] 
end_space_count = 0 
for line in input:
    line = space_count*"-" + line.strip() + end_space_count*"-"
    other_diagonal.append(line)
    space_count -= 1
    end_space_count += 1

count += count_cols(other_diagonal)

print("TOTAL: " + str(count))