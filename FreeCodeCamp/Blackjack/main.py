import random

cards =[]
suits = ["spades", "hearts", "diamonds", "clubs"]
ranks = ["A", "2", "3", "4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
        # print(suit + rank)
        # cards.append(suit + rank)

# print(cards)

random.shuffle(cards)
# print(cards)

card = cards.pop()
print(card)




# suit = suits[1]
# rank = "K"
# value = 10

# print("Your card is: " + rank + " of " + suit)

# suits.append("snakes")



