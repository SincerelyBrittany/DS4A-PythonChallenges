# Variables and Functions
# Python use underscores when naming variables.

# player_choice = "rock"
# computer_choice ="paper"

# Function - set of code that only runs when it is called
# indentation is very important for python

def get_choices():
  player_choice = "rock"
  computer_choice ="paper"

  choices = {"player": player_choice, "computer": computer_choice}

  return player_choice

# Call the get_choices function and store the response in a variable called choices then print it 

get_choice = get_choices()
print(get_choice)


# Dictionaries in python are used to store data data values in key-value pairs 
# dict = {"name" : "brittany", "color": "red", "choice": choices}





# RPS - Calling Functions

def greeting():
  return "Hi"

# Call the function

response = greeting()
print(response)


