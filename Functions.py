# For unknown arguments in a function
def myfunc(**name):
    print(name["fname"]+" "+name["lname"])


myfunc(fname="Emily", lname="Scott")

def func(*kids):
    print("His name is: "+ kids[1])


func("Mark", "Harvey", "Louis")

# Recursion
def recu(k):
    if(k > 0):
        result = k + recu(k-1)
        print(result)
    else:
        result = 0
    return result

print("The Recursion Example Results \n")
recu(3)
