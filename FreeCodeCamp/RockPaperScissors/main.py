# Variables and Functions
# Python use underscores when naming variables.

# player_choice = "rock"
# computer_choice ="paper"

# Function - set of code that only runs when it is called
# indentation is very important for python

def get_choices():
  player_choice = "rock"
  computer_choice ="paper"

  return player_choice

# Call the get_choices function and store the response in a variable called choices then print it 

choices = get_choices()
print(choices)



# RPS - Calling Functions

def greeting():
  return "Hi"

# Call the function

response = greeting()
print(response)


