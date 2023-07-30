# They allow you to create immutable groups of objects. This means that once a tuple is created, it can't be modified. You can't add or remove items.

# They are created in a way similar to lists, but using parentheses instead of square brackets:

names = ("Roger", "Syd")
# A tuple is ordered, like a list, so you can get its values by referencing an index value:

names[0] # "Roger"
names[1] # "Syd"
# You can also use the index() method:

names.index('Roger') # 0
names.index('Syd')   # 1
# As with strings and lists, using a negative index will start searching from the end:

names[-1] # True
# You can count the items in a tuple with the len() function:

len(names) # 2
# You can check if an item is contained in a tuple with the in operator:

print("Roger" in names) # True
# You can also extract a part of a tuple, using slices:

names[0:2] # ('Roger', 'Syd')
names[1:] # ('Syd',)
# Get the number of items in a tuple using the len() global function, the same we used to get the length of a string:

len(names) #2
# You can create a sorted version of a tuple using the sorted() global function:

sorted(names)
# You can create a new tuple from existing tuples using the + operator:

newTuple = names + ("Vanille", "Tina")
print(newTuple)

#Tuples are more memory efficient than the lists. 
# When it comes to the time efficiency, 
# tuples have a slight advantage over the lists 
# especially when we consider lookup value.
#  If you have data that shouldn't change, 
# you should choose tuple data type over lists.