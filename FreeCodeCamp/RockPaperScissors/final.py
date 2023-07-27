import random 

def check_win(player, computer):
  
  print(player, computer)

def get_choices():
  player_choice = input("Enter A Choice: rock, paper, scissors: ")

  computer_choice = random.choice(["rock", "paper", "scissors"])
  choices = {"player": player_choice, "computer": computer_choice}

  check_win(choices["player"], choices["computer"])
  
get_choice = get_choices()
print(get_choice)

  