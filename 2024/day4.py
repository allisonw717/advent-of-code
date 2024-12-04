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


#Part 2 is a different problem :| 
def is_x_mas(grid, i,j):
    a = ""
    b = ""
    a += grid[i-1][j-1]
    a += grid[i][j]
    a += grid[i+1][j+1]
    b += grid[i+1][j-1]
    b += grid[i][j]
    b += grid[i-1][j+1]
    
    if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
        return True
    return False

char_matrix = [] 
for row in input:
    char_matrix.append(list(row.strip()))

#check the inside for A's 
count2 = 0 
countA = 0 
for i, row in enumerate(char_matrix):
    for j, col in enumerate(row):
        if char_matrix[i][j] == 'A':
            countA += 1
            try:
                if is_x_mas(char_matrix,i,j) and i!=0 and j!=0 and i!= len(row)-1 and j!=len(char_matrix)-1:
                    count2 += 1
            except:
                break

print("TOTAL2: " + str(count2))
print(countA)


#1850 < ans < 1912