# import random 

# def start_game(): 
#   get_choice = get_choices()
#   print(get_choice)

# def check_win(player, computer):
# #   print("You Chose " + player + "Computer Chose " + computer)
#   print(f"You chose {player} and the computer chose {computer}")
#   if player == "rock" and computer == "scissors":
#     print("You win")
#     return
#   elif player == "scissors" and computer == "rock":
#     print("You Lose")
#     return
#   elif player == "paper" and computer == "rock":
#     print("You Win")
#     return
#   elif player == "rock" and computer == "paper":
#     print("You Lose")
#     return
#   elif player == "scissors" and computer == "paper":
#     print("You Win")
#     return
#   elif player == "paper" and computer == "scissors":
#     print("You Lose")
#     return
#   elif player == computer:
#     print("Tie")
#     return start_game()
#   else:
#     print("Try again")
#     print(player, computer)
#     return

# def get_choices():
#   player_choice = input("Enter A Choice: rock, paper, scissors: ")

#   computer_choice = random.choice(["rock", "paper", "scissors"])
#   choices = {"player": player_choice, "computer": computer_choice}

#   check_win(choices["player"], choices["computer"])


# start_game()


import random 

def start_game(): 
  get_choice = get_choices()
  print(get_choice)

def check_win(player, computer):
#   print("You Chose " + player + "Computer Chose " + computer)
  print(f"You chose {player} and the computer chose {computer}")
  if player == "rock" and computer == "scissors":
    print("You win")
    return
  elif player == "scissors" and computer == "rock":
    print("You Lose")
    return
  elif player == "paper" and computer == "rock":
    print("You Win")
    return
  elif player == "rock" and computer == "paper":
    print("You Lose")
    return
  elif player == "scissors" and computer == "paper":
    print("You Win")
    return
  elif player == "paper" and computer == "scissors":
    print("You Lose")
    return
  elif player == computer:
    print("Tie")
    return start_game()
  else:
    print("Try again")
    print(player, computer)
    return

def get_choices():
  player_choice = input("Enter A Choice: rock, paper, scissors: ")

  computer_choice = random.choice(["rock", "paper", "scissors"])
  choices = {"player": player_choice, "computer": computer_choice}

  check_win(choices["player"], choices["computer"])


start_game()


  