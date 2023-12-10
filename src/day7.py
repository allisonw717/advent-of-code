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
        self.original_cards = [x for x in self.cards]
        self.bid = int(bid)
        self.strength = self.get_strength()
    
    def __str__(self):
        string = str(self.original_cards) + ": "+ str(self.bid)
        return string
    
    #five: 7, four:6, full:5, three:4, two:3, one:2, high:1
    def get_strength_no_joker(self):
        counts = sorted(Counter(self.cards).values(), reverse=True)
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
    
    def get_strength(self):
        if self.joker and 1 in self.cards:
            #card with most occurences first, then on 
            cards_by_freq = sorted(Counter(self.cards), reverse=True)
            if cards_by_freq[0] != 1:
                assert Counter(self.cards).most_common != 1
                self.cards = [cards_by_freq[0] if item == 1 else item for item in self.cards]
            elif len(cards_by_freq) != 1:
                assert Counter(self.cards).most_common == 1
                self.cards = [cards_by_freq[1] if item == 1 else item for item in self.cards]
            else:
                assert self.cards == [1] * 5
        return self.get_strength_no_joker()

    def __gt__(self, other):
        if self.strength == other.strength:
            for i in range(0,5):
                assert self.original_cards[i] != 11, f"self.original_cards had 11 - {self.original_cards}"
                assert other.original_cards[i] != 11, f"other.original_cards had 11 - {other.original_cards}"
                if self.original_cards[i] != other.original_cards[i]:
                    return self.original_cards[i] > other.original_cards[i]
            assert False
            return False
        return self.strength > other.strength

hands = [] 
joker_hands = [] 
for line in lines:
    cards, bid = line.split()
    hands.append(hand(cards, bid))
    joker_hands.append(hand(cards,bid,True))

#PART 1
# winnings = 0 
# for i, hand in enumerate(sorted(hands)):
#     winnings += hand.bid * (i + 1)
# if winnings == 250898830:
#     print("congrats didn't break part one")
# else:
#     print("broke part 1 smh")

#PART 2
winnings_with_joker = 0 
for i, hand in enumerate(sorted(joker_hands)):
    print(hand)
    winnings_with_joker += hand.bid * (i + 1)

print(winnings_with_joker)

#251976591 too low 
#251828497 ... got lower ??? 