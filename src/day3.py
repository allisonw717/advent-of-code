import helpers

helpers.set_file_reader()
f = open('day3.txt') 
lines = f.readlines()

class grid_number: 
    def __init__(self, value, coords):
        self.coords = coords
        self.length = len(coords)
        self.value = int(value)
    def __str__(self):
        print_me = "" 
        for coord in self.coords:
            print_me += str(coord[0]) + str(coord[1]) + " "
        return print_me
    def get_surrounding_indices(self):
        #LMAOOO DON'T EVEN ASK 
        result = [] 
        top_left = (self.coords[0][0] - 1, self.coords[0][1] - 1)
        top_right = (self.coords[self.length - 1][0] - 1, self.coords[self.length - 1][1] + 1)
        result.extend(list(zip([top_left[0]] * (self.length + 2),list(range(top_left[1],top_right[1] + 1)))))
        result.append((self.coords[0][0], self.coords[0][1] - 1))
        result.append((self.coords[self.length - 1][0], self.coords[self.length - 1][1] + 1))
        bottom_left = (self.coords[0][0] + 1, self.coords[0][1] - 1)
        bottom_right = (self.coords[self.length - 1][0] + 1, self.coords[self.length - 1][1] + 1)
        result.extend(list(zip([bottom_left[0]] * (self.length + 2), list(range(bottom_left[1],bottom_right[1] + 1)))))
        return result

line_of_dots = ["."] * (len(lines[0].strip()) + 2)
grid = [] 
grid.append(line_of_dots)
for line in lines:
    line = "." + line.strip() + "."
    grid.append([*line.strip()])
grid.append(line_of_dots)

numbers = []
stars = {} 
for i, row in enumerate(grid):
    last_was_number = False
    current_number_coords = [] 
    number_value = ""
    for j, item in enumerate(row): 
        if item.isnumeric():
            current_number_coords.append((i,j))
            number_value += item 
        else:
            if current_number_coords:
                numbers.append(grid_number(number_value, current_number_coords))
            current_number_coords = [] 
            number_value = ""
            if item == "*":
                stars[(i,j)] = [] 


sum = 0 
sum_part_two = 0 
for num in numbers:
    for coord in num.get_surrounding_indices():
        if grid[coord[0]][coord[1]] != ".":
            sum += num.value
            if grid[coord[0]][coord[1]] == "*":
                stars[(coord[0],coord[1])].append(num.value)
            break 

for star, numbers in stars.items():
    if len(numbers) == 2:
        sum_part_two += numbers[0] * numbers[1]

print(sum)
print(sum_part_two)







