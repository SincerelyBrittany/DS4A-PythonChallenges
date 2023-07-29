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

