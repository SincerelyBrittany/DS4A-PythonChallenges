# In a Python command line application you can display information to the user using the print() function:

name = "Roger"
print(name)
# We can also accept input from the user, using input():

print('What is your age?')
age = input()
name = input("What is your name")
print('Your age is ' + age)
print('Your name is ' + name)

#This approach gets input at runtime, meaning the program will stop execution and will wait until the user types something and presses the enter key.

#You can also do more complex input processing and accept input at program invocation time, and we'll see how to do that later on.