import helpers

helpers.set_file_reader()
f = open('day4.txt') 
lines = f.readlines()

score = 0 
card_count = [1] * (len(lines))
for index, line in enumerate(lines):
    card_num, numbers = line.strip().split(":")
    winning_numbers, my_numbers = numbers.split("|")
    winning_numbers = [int(x) for x in winning_numbers.strip().split()]
    my_numbers = [int(x) for x in my_numbers.strip().split()]
    for copy in range(0,card_count[index]):
        win_multiplier = 0
        num_wins = 0 
        for num in my_numbers:
            if num in winning_numbers:
                num_wins += 1
                card_count[index + num_wins] += 1
                if(win_multiplier == 0): #ew lol 
                    win_multiplier = 1
                else:
                    win_multiplier*=2
    score += win_multiplier

print(score)
print(sum(card_count))

