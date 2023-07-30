#A function lets us create a set of instructions that we can run when needed.
# Functions are essential in Python and in many other programming languages. They help us create meaningful programs, because they allow us to decompose a program into manageable parts, and they promote readability and code reuse.

#Here is an example function called hello that prints "Hello!":

def hello():
    print('Hello!')
#This is the function definition. Thereis a name (hello) and a body, the set of instructions, which is the part that follows the colon. It's indented one level on the right.

#To run this function, we must call it. This is the syntax to call the function:

hello()
#We can execute this function once, or multiple times.

#The name of the function, hello, is very important. It should be descriptive, so anyone calling it can imagine what the function does.

#A function can accept one or more parameters:

def hello(name):
    print('Hello ' + name + '!')
#In this case we call the function by passing the argument

hello('Roger')
#We call parameters the values accepted by the function inside the function definition, and arguments the values we pass to the function when we call it. It's common to get confused about this distinction.

#An argument can have a default value that's applied if the argument is not specified:

def hello(name='my friend'):
    print('Hello ' + name + '!')

hello()
#Hello my friend!
#Here's how we can accept multiple parameters:

def hello(name, age):
    print('Hello ' + name + ', you are ' + str(age) + ' years old!')
#In this case we call the function passing a set of arguments:

hello('Roger', 8)
#Parameters are passed by reference. All types in Python are objects, but some of them are immutable, including integers, booleans, floats, strings, and tuples. This means that if you pass them as parameters and you modify their value inside the function, the new value is not reflected outside of the function:

def change(value):
    value = 2

val = 1
change(val)

print(val) #1
#If you pass an object that's not immutable, and you change one of its properties, the change will be reflected outside.

#A function can return a value, using the return statement. For example in this case we return the name parameter name:

def hello(name):
    print('Hello ' + name + '!')
    return name
#When the function meets the return statement, the function ends.

#We can omit the value:

def hello(name):
    print('Hello ' + name + '!')
    return
#We can have the return statement inside a conditional, which is a common way to end a function if a starting condition is not met:

def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')
#If we call the function passing a value that evaluates to False, like an empty string, the function is terminated before reaching the print() statement.

#You can return multiple values by using comma separated values:

def hello(name):
    print('Hello ' + name + '!')
    return name, 'Roger', 8
#In this case calling hello('Syd') the return value is a tuple containing those 3 values: ('Syd', 'Roger', 8).


# Nested Functions - functions can be nested within another function

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ') #split - creates a list out of the string
    for word in words:
        say(word)

talk("I am going to buy the milk")

def count():
    count = 0

    def increment():
        nonlocal count # nonlocal allows you to use out of scope variables - helpws with closures
        count = count + 1
        print(count)
    increment()

count()


# Closure example

def counter():
    count = 0

    def increment():
        nonlocal count # nonlocal allows you to use out of scope variables - helpws with closures
        count = count + 1
        return count
    return increment

increment = counter()

print(increment())

print(increment())

print(increment())


