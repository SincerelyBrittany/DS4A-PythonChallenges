# Everything in Python is an object.

#Even values of basic primitive types (integer, string, float..) are objects. Lists are objects, as are tuples, dictionaries, everything.

#Objects have attributes and methods that can be accessed using the dot syntax.

#For example, try defining a new variable of type int:

age = 8
#age now has access to the properties and methods defined for all int objects.

#This includes, for example, access to the real and imaginary part of that number:

print(age.real) # 8
print(age.imag) # 0

print(age.bit_length()) #4

# the bit_length() method returns the number of bits necessary to represent this number in binary notation
#A variable holding a list value has access to a different set of methods:

items = [1, 2]
items.append(3)
items.pop()
#The methods depend on the type of value.

#The id() global function provided by Python lets you inspect the location in memory for a particular object.

id(age) # 140170065725376
#Your memory value will change - I am only showing it as an example.

#If you assign a different value to the variable, its address will change, because the content of the variable has been replaced with another value stored in another location in memory:

age = 8

print(id(age)) # 140535918671808

age = 9

print(id(age)) # 140535918671840
#But if you modify the object using its methods, the address stays the same:

items = [1, 2]

print(id(items)) # 140093713593920

items.append(3)

print(items) # [1, 2, 3]
print(id(items)) # 140093713593920
#The address only changes if you reassign a variable to another value.

#Some objects are mutable, while others are immutable. This depends on the object itself.

#If the object provides methods to change its content, then it's mutable. Otherwise it's immutable.

#Most types defined by Python are immutable. For example an int is immutable. There are no methods to change its value. If you increment the value using

age = 8
age = age + 1

#or

age += 1
#and you check with id(age), you will find that age points to a different memory location. The original value has not mutated, we just switched to another value.