# Dictionaries are a very important Python data structure.

# While lists allow you to create collections of values, dictionaries allow you to create collections of key / value pairs.

# Here is a dictionary example with one key/value pair:

dog = { 'name': 'Roger' }
# The key can be any immutable value like a string, a number or a tuple. The value can be anything you want.

# A dictionary can contain multiple key/value pairs:

dog = { 'name': 'Roger', 'age': 8 , 'breed': "dog"}
# You can access individual key values using this notation:

dog['name'] # 'Roger'
dog['age']  # 8
# Using the same notation you can change the value stored at a specific index:
print(dog)

dog['name'] = 'Syd'
# And another way is using the get() method, which has an option to add a default value:

print(dog)

dog.get('name') # 'Roger'
print(dog.get('color'))
print(dog.get('color', "brown"))
dog.get('test', 'default') # 'default'
# The pop() method retrieves the value of a key, and subsequently deletes the item from the dictionary:

print(dog.pop('name')) # 'Roger'
# The popitem() method retrieves and removes the last key/value pair inserted into the dictionary:

print(dog.popitem())
# You can check if a key is contained into a dictionary with the in operator:

print(dog)

print('name' in dog) # True
#  Get a list with the keys in a dictionary using the keys() method, passing its result to the list() constructor:

list(dog.keys()) # ['name', 'age']
# Get the values using the values() method, and the key/value pairs tuples using the items() method:

print(list(dog.values()))
# ['Roger', 8]

print(list(dog.items()))
# [('name', 'Roger'), ('age', 8)]
# Get a dictionary length using the len() global function, the same we used to get the length of a string or the items in a list:

len(dog) #2
# You can add a new key/value pair to the dictionary in this way:

dog['favorite food'] = 'Meat'

# You can remove a key/value pair from a dictionary using the del statement:
del dog['favorite food']
 
# To copy a dictionary, use the copy() method:

dogCopy = dog.copy()