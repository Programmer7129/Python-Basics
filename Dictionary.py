# Syntax for creating a dictionary is:
thisdict = {
    "brand": "Ford",
    "Name": "Mustang",
    "Year": 1967
}
print(thisdict["Year"])

# Nesting Dictionaries
child1 = {
    "Name": "Louis",
    "Age": 20
}
child2= {
    "Name": "Mark",
    "Age": 20
}
child3 = {
    "Name": "Harvey",
    "Age": 20
}
dict = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(dict["child2"])
