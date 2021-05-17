# Multi line Strings
# Use Three double quotes or single quote to save multi line string
a = """Jfiuwhfwv
fvjnefvnevnfvnfvn
owjvnjnvfeivnvefjvn
vfvjnfvnonv"""
print(a)

# Strings are Arrays
b = "Hello, World!"
print("Output is : " + b[5])

# Looping through Strings
for x in "banana":
    print(x)

# Slicing Strings
c = "Hello World!"
print(c[2:7])  # Here the letter with index 7 won't be included
print(c[-2:-1])  # Negative represents from the end.

# Strip Keyword
# It removes whitespaces from the beginning and the end
d = " Hello World! "
print(d)
print(d.strip())

# Replace String
x = "Hello World!"
print(x.replace("H", "J"))

# Split String
y = "Hello, World!"
print(y.split(","))  # When this separator is found python will split the strings

# Format String
quantity = 3
itemno = 567
price = 50.00
myorder = "I want {} pieces of item {} for {} dollars"
modifiedorder= "I want to pay {2} dollars for {0} pieces of item {1}."

print(myorder.format(quantity, itemno, price))
print(modifiedorder.format(quantity, itemno, price))

# Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
