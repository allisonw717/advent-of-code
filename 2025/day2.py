f = open('2025/input.txt') 
input = f.readline()


ranges = input.split(",")
idk = [x.split("-") for x in ranges]

product_ints = []
for str_pair in idk: 
    start, end = int(str_pair[0]),  int(str_pair[1])
    product_ints.append([start,end])

def part1(): 
    invalid_total = 0 
    for product_range in product_ints:
        for product_id in range(product_range[0], product_range[1]+1):
            id_string = str(product_id)
            midpoint = len(id_string)//2
            if id_string[:midpoint] == id_string[midpoint:]:
                invalid_total += product_id

    print(invalid_total)


#mmmm for loops 
def part2():
    invalid_total = 0 
    for product_range in product_ints:
        for product_id in range(product_range[0], product_range[1]+1):
            id_string = str(product_id)
            midpoint = len(id_string)//2
            for pattern_length in range(1,midpoint+1):
                #is the rest of the substring[moving through it] the same as the first one
                first = id_string[0:pattern_length] 
                diff = False
                for start_index in range(0,len(id_string)-pattern_length+1,pattern_length):
                    if id_string[start_index: start_index+pattern_length] != first: 
                        diff = True 
                if not diff and len(id_string) % pattern_length == 0:
                    invalid_total += product_id
                    break


    print(invalid_total)    

part2()




