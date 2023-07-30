name = "SincerelyBrittany"
age = 25

# Cant use keywords
# Cant use symbols 


# Expressions and Statements 
# expressions - any type of code that returns a value 

# Example:
1+1
"sincereybrittany"

# statement is an operation on a value , does something to the value
# examples: 
name = "sincerelybritany"
print(name)

name = "sincerelybritany"; print(name)


print("""
This is a multi-line string
      
and you can see the space

""")

# Indentation - you cant randomly indent 

# DataTypes
# Can check the type or isinstance
print(type(name))
print(type(name) == str)
print(isinstance(name, str))

#Floats 
num = 2.5
print(isinstance(age, int))
print(isinstance(age, float))
print(isinstance(num, float))

make_Int_A_Float = float(2) # casting
print(isinstance(make_Int_A_Float, float))

make_string_an_int = "20"
print(isinstance(make_string_an_int, int))

make_string_an_int = int("20") #casting
print(isinstance(make_string_an_int, int))


# complex for complex numbers
# bool for booleans 
# list for lists 
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

#Arithmetic 

1 + 1
2 - 1
2 * 2
4 / 2 
4 % 3 # 1 
4 ** 2
5 // 2 #2 - floor division
1 + -1 # 0

print("Autumn" + "is a good dog")

age = 8 
age += 8 # age = age + 8

print(age)

#COmparison 
a = 1
b = 2

a == b
a != b
a > b
a < b
a <= b
a >= b

#Boolean operators 

condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True


print( 0 or 1) ## 1
print (False or 'hey') # hey
print ('hi' or 'hey') # 'hi
print ([] or False) ## False because [] is a falsy value
print (False or []) # []

print( 0 and 1) ## 0
print( 1 and 0) ## 0
print (False and 'hey') # false
print ('hi' and 'hey') # 'hey
print ([] and False) ## []
print (False or []) # false

# Bitwise operators 

# & - performs binary AND 
# | - performs binary or
# ^ - performs a binary XOR operation
# ~ - performs a binary NOT operation
# << - shift left operation
# >> - shift right operation


# is - identity operation - compares to objects and returns true if both are the same
# in - membership operator - tells if a value is contained in a list or another sequence 

# ternary operator - quickly define a conditional
# example:

def is_adult(age):
    if age > 18:
        return True
    else: 
        return False
    
def is_adult2(age): 
    return True if age > 18 else False

a = 2
result = 2 if a == 0 else 3
print(result) # 3


print("SincerlyBrittanyUsingTheUpperMethod".upper())
print("sincerlyBrittanyUsingTheTitleMethod".title())
print("sincerlyBrittanyUsingTheTitleMethod".islower())

# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is not empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get an uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startsswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific character separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the position of a substring


#THESE ALL RETURN A NEW STRING/ Not the modified string

name = "cat"
print(len(name)) #finds the length os a string 
print ("au" in name) #checks to see if au is in the name

#ESCAPING characters

name = "Br\"au"
print(name)
name = 'Br\"au'
print(name)
name = 'Br\'"au'
print(name)
name = 'Br\nau' #adds a new line
print(name)
name = "this will show a slice string - check it out"
print(name[1:8])
print(name[10:])

# numbers are always true except for the number 0
# strings are false - only when empty 
# list, tuples, and dictionaries are only false when empty

#When evaluating a value for True or False, if the value is not a bool we have some rules depending on the type we're checking:

#numbers are always True except for the number 0
#strings are False only when empty
#lists, tuples, sets, and dictionaries are False only when empty

#The global any() function is also very useful when working with booleans, as it returns True if any of the values of the iterable (list, for example) passed as argument are True:


book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

# The global all() function is same, but returns True if all of the values passed to it are True:

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])

# Complex numbers in Python
# Complex numbers are of type complex.

# You can define them using a value literal:

complexNumber = 2+3j
# or using the complex() constructor:

complexNumber = complex(2, 3)
# Once you have a complex number, you can get its real and imaginary part:

complexNumber.real #2.0
complexNumber.imag #3.0

# Again, to check if a variable is of type complex, you can use the type() global function:

type(complexNumber) == complex #True

# abs() returns the absolute value of a number.

# round() given a number, returns its value rounded to the nearest integer:

round(0.12) #0
# You can specify a second parameter to set the decimal point's precision:

round(0.12, 1) #0.1
# Several other math utility functions and constants are provided by the Python standard library:

# the math package provides general math functions and constants
# the cmath package provides utilities to work with complex numbers.
# the decimal package provides utilities to work with decimals and floating point numbers.
# the fractions package provides utilities to work with rational numbers.