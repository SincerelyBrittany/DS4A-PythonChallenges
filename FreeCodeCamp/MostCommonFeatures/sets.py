#Sets are another important Python data structure.

#We can say they work like tuples, but they are not ordered, and they are mutable.

#Or we can say they work like dictionaries, but they don't have keys.

#They also have an immutable version, called frozenset.

#You can create a set using this syntax:

names = {"Roger", "Syd"}
#Sets work well when you think about them as mathematical sets.

#You can intersect two sets:

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2 #{'Roger'}
print(intersect)
#You can create a union of two sets:

set1 = {"Roger", "Syd"}
set2 = {"Luna"}

union = set1 | set2
#{'Syd', 'Luna', 'Roger'}
#You can get the difference between two sets:

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

difference = set1 - set2 #{'Syd'}
#You can check if a set is a superset of another (and of course if a set is a subset of another):

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

isSuperset = set1 > set2 # True
#You can count the items in a set with the len() global function:

names = {"Roger", "Syd"}
len(names) # 2
#You can get a list from the items in a set by passing the set to the list() constructor:

names = {"Roger", "Syd"}
list(names) #['Syd', 'Roger']
#You can check if an item is contained in a set with the in operator:

print("Roger" in names) # True


mod = set1 + set2 #a union
mod = set1 - set2 
mod = set1 > set2 
mod = set1 < set2 
print(mod)

#A set can not have two of the same thing