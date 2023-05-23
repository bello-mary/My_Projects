varOne = 10 # Global variable

def printValue():
    varTwo = 20 # varTwo is considered local variable to print value function
    varThree = 30 # varThree is considered local variable to print value function
    print(varTwo)
    print(varThree)
   # varOne = 15 # I an declaring a new local variable called varOne
    print(varOne)
    




printValue() # calling the function printValue()
print(varOne) # printing the global variable