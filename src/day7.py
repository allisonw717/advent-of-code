import helpers
from collections import Counter

helpers.set_file_reader()
f = open('day7.txt') 
lines = f.readlines()
    
class hand: 
    
    letters = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    
    def __init__(self, cards, bid, joker = False):
        self.joker = joker
        self.cards = [] 
        for card in cards:
            if card in self.letters.keys():
                if self.joker and card == 'J':
                    self.cards.append(1)
                else:
                    self.cards.append(self.letters[card])
            else:
                self.cards.append(int(card))
        self.bid = int(bid)
        self.strength = self.get_strengh()
    
    def __str__(self):
        string = str(self.cards) + ": "+ str(self.bid)
        return string
    
    #five: 7, four:6, full:5, three:4, two:3, one:2, high:1
    def get_strengh(self):
        counts = sorted(Counter(self.cards).values(), reverse=True)
        if self.joker and 1 in self.cards:
             counts[0] += self.cards.count(1)
        if counts[0] == 5:
            return 7
        if counts[0] == 4:
            return 6
        if counts[0] == 3:
            if counts[1] == 2:
                return 5
            return 4
        if counts[0] == 2:
            if counts[1] == 2:
                return 3
            return 2
        return 1   
    
    def __gt__(self, other):
        if self.strength == other.strength:
            for i in range(0,5):
                if self.cards[i] != other.cards[i]:
                    return self.cards[i] > other.cards[i]
            return False
        return self.strength > other.strength

hands = [] 
joker_hands = [] 
for line in lines:
    cards, bid = line.split()
    hands.append(hand(cards, bid))
    joker_hands.append(hand(cards,bid,True))

#PART 1
winnings = 0 
for i, hand in enumerate(sorted(hands)):
    winnings += hand.bid * (i + 1)

#PART 2
winnings_with_joker = 0 
for i, hand in enumerate(sorted(joker_hands)):
    print(hand)
    winnings_with_joker += hand.bid * (i + 1)

print(winnings)
print(winnings_with_joker)
