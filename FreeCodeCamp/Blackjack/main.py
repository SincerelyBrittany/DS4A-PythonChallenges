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

def shuffle():
    random.shuffle(cards)
  

shuffle()
# print(cards)

def deal(num):
    cards_dealt = []
    for x in range(num):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

cards_dealt = deal(2)
# print(cards_dealt)

card = cards_dealt[0]
rank = card[1]

if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank =="K":
    value = 10
else:
    value = rank


print(rank, value)


print(rank)




# suit = suits[1]
# rank = "K"
# value = 10

# print("Your card is: " + rank + " of " + suit)

# suits.append("snakes")



