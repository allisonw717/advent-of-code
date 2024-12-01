import helpers

helpers.set_file_reader()
f = open('day1.txt') 
lines = f.readlines()

#PART 1
sum = 0 
for line in lines:
    number_string = ""
    for letter in line:
        if letter.isnumeric():
            number_string += letter
    #sum += int(number_string[0] + number_string[-1])
    
print(sum)

#PART 2
number_words = ["one","two","three","four","five","six","seven","eight","nine"]
get_numeral = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
sum = 0 
for line in lines:
    numbers = [] 
    for index, letter in enumerate(line):
        if letter.isnumeric():
            numbers.append(letter)
        else:
            for word in number_words:
                if line[index:].startswith(word):
                    numbers.append(get_numeral[word])
    hehe_string = numbers[0] + numbers[-1]
    sum += int(hehe_string)
    
print(sum)
#54673 is too high 





