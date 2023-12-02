import helpers
from functools import reduce

helpers.set_file_reader()
f = open('day2.txt') 
lines = f.readlines()

#PART 1
max_dice = {
    'red':12,
    'green':13,
    'blue':14
}

cursed_sum = 0 
for line in lines:
    game, dice = line.split(":")
    game_id = game.split(" ")[1]
    dice_by_round = dice.split(";")
    possible = True 
    for round in dice_by_round:
        dice_info = [x.strip() for x in round.split(",")]
        for dice in dice_info:
           count, color = dice.split(" ")
           if int(count) > max_dice[color]:
               possible = False 
    if possible:
        cursed_sum += int(game_id)

print(cursed_sum)

#PART 2
cursed_cursed_sum = 0 
for line in lines:
    max_dice = {
        'red':0,
        'green':0,
        'blue':0
    }
    game, dice = line.split(":")
    game_id = game.split(" ")[1]
    dice_by_round = dice.split(";")
    possible = True 
    for round in dice_by_round:
        dice_info = [x.strip() for x in round.split(",")]
        for dice in dice_info:
           count, color = dice.split(" ")
           if max_dice[color] < int(count):
               max_dice[color] = int(count) 
    cursed_cursed_sum += reduce(lambda x, y: x*y, max_dice.values())
    
print(cursed_cursed_sum)
