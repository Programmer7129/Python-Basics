# Lists Comprehension
# It is a shorter syntax when you want to create a new list based on the values of an existing list.

# This is a illustration of a simple program.
fruits = ["Orange", "Mango", "Kiwi", "Banana"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension of we can write this in 1 line of code.
fruits = ["Orange", "Mango", "Kiwi", "Banana"]

listnew = [x for x in fruits if "a" in x]
print(listnew)

# listnew = [expression for item in iterable if condition == True]

UpperList = [x.upper() for x in fruits]
print(UpperList)

# Sort List
# Using Sort function can sort list alphanumerically
# To sort descending use keyword argument revere = True

thislist = ["banana", "apple", "kiwi", "orange", "watermelon"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# Customizing Sort function
def myfunc(n):
    return abs(n-50)


nlist = [100, 50, 70, 60, 80, 40]

nlist.sort(key=myfunc)

print(nlist)


# If list has both upper case and lower case words then make sure to use str.lower keyword in key
list1 = ["banana", "apple", "Kiwi", "Orange", "watermelon"]
list1.sort(key=str.lower)
print(list1)
