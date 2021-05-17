# Tuples are ordered, unchangeable
# If we want to create a tuple with only one item then we need to add a comma at the end.

mytuple = ("apple",)

# Incorrect syntax
# mytuple = ("apple")

# If we want to add or remove an item from a tuple we first need to convert it to list adn then convert it back to tuple

# Unpack tuples
fruits = ["banana", "apple", "orange", "kiwi", "mango", "watermelon"]
(yellow, red, orange, *green) = fruits
print(yellow)
print(red)
print(orange)
print(green)

