# Lists are an essential Python data structure.

# The allow you to group together multiple values and reference them all with a common name.

# For example:

dogs = ["Roger", "Syd"]
# A list can hold values of different types:

items = ["Roger", 1, "Syd", True]
# You can check if an item is contained in a list with the in operator:

print("Roger" in items) # True
print("Britt" in items) #False


# A list can also be defined as empty:

# items = []
# You can reference the items in a list by their index, starting from zero:

items[0] # "Roger"
items[1] # 1
items[3] # True

# Using the same notation you can change the value stored at a specific index:

items[0] = "Roger"

# You can also use the index() method:

#dogs.index(0) # "Roger"
#items.index(1) # 1
# As with strings, using a negative index will start searching from the end:

items[-1] # True
# You can also extract a part of a list, using slices:

items[0:2] # ["Roger", 1]
items[2:] # ["Syd", True]
# Get the number of items contained in a list using the len() global function, the same we used to get the length of a string:

len(items) #4
# You can add items to the list by using a list append() method:

items.append("Test")
# or the extend() method:

items.extend(["Test"])
# You can also use the += operator:

items += ["Test"]

# items is ['Roger', 1, 'Syd', True, 'Test']
# Tip: with extend() or += don't forget the square brackets. Don't do items += "Test" or items.extend("Test") or Python will add 4 individual characters to the list, resulting in ['Roger', 1, 'Syd', True, 'T', 'e', 's', 't']

# Remove an item using the remove() method:

items.remove("Test")
# You can add multiple elements using

items += ["Test1", "Test2"]

#or

items.extend(["Test1", "Test2"])
# These append the item to the end of the list.

# To add an item in the middle of a list, at a specific index, use the insert() method:

items.insert("Test", 1) # add "Test" at index 1
# To add multiple items at a specific index, you need to use slices:

items[1:1] = ["Test1", "Test2"]
# Sort a list using the sort() method:

items.sort()
# Tip: sort() will only work if the list holds values that can be compared. Strings and integers for example can't be compared, and you'll get an error like TypeError: '<' not supported between instances of 'int' and 'str' if you try.

# The sort() methods orders uppercase letters first, then lowercase letters. To fix this, use:

items.sort(key=str.lower)
# instead.

# Sorting modifies the original list content. To avoid that, you can copy the list content using

itemscopy = items[:]
# or use the sorted() global function:

print(sorted(items, key=str.lower))
# that will return a new list, sorted, instead of modifying the original list.

print(dogs.pop()) #return and remove last item from the list
print(dogs)

names = ["Zebra", "cat", "Apple", "bat", "bear", "Beatle"]
namesCopy = names[:]

print(names.sort())
print(names.sort(key=str.lower()))
print(namesCopy)

sorted(namesCopy, key=str.lower())