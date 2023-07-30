from enum import Enum

#Python has no way to enforce that a variable should be a constant.

#The nearest you can get is to use an enum:

class Constants(Enum):
    WIDTH = 1024
    HEIGHT = 256
#And get to each value using, for example, Constants.WIDTH.value.

#No one can reassign that value.

#Otherwise if you want to rely on naming conventions, you can adhere to this one: declare variables that should never change uppercase:

WIDTH = 1024
# No one will prevent you from overwriting this value, and Python will not stop it.

# That's what most Python code does that you will see.


# Then you can initialize a new enum in this way:

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# Once you do so, you can reference State.INACTIVE and State.ACTIVE, and they serve as constants.

# Now if you try to print State.ACTIVE for example:

print(State.ACTIVE)
print(list(State))
print(len(State))
print(State.ACTIVE.value)
print(State(1))
print(State["ACTIVE"])
# it will not return 1, but State.ACTIVE.

# The same value can be reached by the number assigned in the enum: print(State(1)) will return State.ACTIVE. Same for using the square brackets notation State['ACTIVE'].

# You can, however, get the value using State.ACTIVE.value.

# You can list all the possible values of an enum:

list(State) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
# You can count them:

len(State) # 2