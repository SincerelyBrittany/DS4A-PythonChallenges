import random



# Variables and Functions
# Python use underscores when naming variables.

# player_choice = "rock"
# computer_choice ="paper"

# Function - set of code that only runs when it is called
# indentation is very important for python

def get_choices():
  #RPS - User Input
  player_choice = input("Enter A Choice: rock, paper, scissors: ")

  # RPS - importing libraries, creating list, methods
  # Python libraries are a set of useful functions so that you dont have to write code from scratch
  # When you import a code into you program you get access to more features without writing additional code.
  # We will use the random library to get the computer to choose at random (rock paper scissors)

  # computer_choice ="paper"

  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Dictionaries in python are used to store data data values in key-value pairs 
  # example: dict = {"name" : "brittany", "color": "red", "choice": choices}
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

# Call the get_choices function and store the response in a variable called choices then print it 

get_choice = get_choices()
print(get_choice)

# List are used to store multiple items in a single variable
# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)
# print(dinner)

# RPS - Calling Functions

# def greeting():
#   return "Hi"

# Call the function

# response = greeting()
# print(response)


