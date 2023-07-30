import random

class Deck:

    def __init__(self) -> None:   
        self.cards =[]
        suits = ["spades", "hearts", "diamonds", "clubs"]
        ranks = [
                        {"rank": "A", "value": 11},
                        {"rank": "2", "value": 2},
                        {"rank": "3", "value": 3},
                        {"rank": "4", "value": 4},
                        {"rank": "5", "value": 5},
                        {"rank": "6", "value": 6},
                        {"rank": "7", "value": 7},
                        {"rank": "8", "value": 8},
                        {"rank": "9", "value": 9},
                        {"rank": "10", "value": 10},
                        {"rank": "J", "value": 10},
                        {"rank": "Q", "value": 10},
                        {"rank": "K", "value": 10},
                    ]
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])
                # print(suit + rank)
                # cards.append(suit + rank)

        # print(cards)

    def shuffle(self):
        random.shuffle(self.cards)


    def deal(self, num):
        cards_dealt = []
        for x in range(num):
            card = self.cards.pop()
            cards_dealt.append(card)
        return cards_dealt
    

    # shuffle()

    # ## REFACTOR

    # card = deal(1)[0]

    # print(card[1]["value"])
    # #  card 
    # # a deck
    # # a hand




# print(cards)


## BEFORE - REFACTOR

# import random

# cards =[]
# suits = ["spades", "hearts", "diamonds", "clubs"]
# ranks = ["A", "2", "3", "4","5","6","7","8","9","10","J","Q","K"]
# for suit in suits:
#     for rank in ranks:
#         cards.append([suit, rank])
#         # print(suit + rank)
#         # cards.append(suit + rank)

# # print(cards)

# def shuffle():
#     random.shuffle(cards)



# def deal(num):
#     cards_dealt = []
#     for x in range(num):
#         card = cards.pop()
#         cards_dealt.append(card)
#     return cards_dealt

# cards_dealt = deal(2)
# # print(cards_dealt)

# card = cards_dealt[0]
# rank = card[1]

# if rank == "A":
#     value = 11
# elif rank == "J" or rank == "Q" or rank =="K":
#     value = 10
# else:
#     value = rank


# rank_dict = {"rank" : rank, "value": value}

# print(rank_dict["rank"], rank_dict["value"])







# suit = suits[1]
# rank = "K"
# value = 10

# print("Your card is: " + rank + " of " + suit)

# suits.append("snakes")



