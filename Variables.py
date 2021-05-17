# Variable
# We do not need to define the variable type every time we declare one

x = 5
y = "John"  # y = 'John' is also valid
print(x)

# We can print the type of the variable by
print(type(x))

# Casting
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0

# a and A are two different variables


x, y, z = 'Orange', 'Banana', 'Grapes'
# x = Orange
# y = Banana
# z = Grapes

# Also we can unpack a list
fruits =['Apple', 'Banana', 'Orange']
x, y, z = fruits
print(x)  # Apple
print(y)  # Banana
print(z)  # Orange

# Python has a random module for generating random numbers
# import random
# print(random.randrange(1,10))

