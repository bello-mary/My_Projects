# Name: Mary Bello
# Student ID: W0451351
#Assignment 3.

#write a loop statement that print:
# All positive numbers that are divisible by 10 and less than n.
#Note: Use a function called printPositiveNumbers to perform this loop by passing the value of n
print("=====================================================================")
def printPositiveNumber():
    num = 1
    output = ""
    while num <=100:
        if num % 10 == 0:
            output += str(num) + " , "
            #print(num)
        num += 1
    print(output)
printPositiveNumber()

print("=====================================================================")

#All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64.
#Note: Use a function called printPowersOfTwo to perform this loop by passing the value of n.
def printPowersOfTwo(): 
    n = 2
    exponent = 0
    while exponent < 7:
        j = n ** exponent
        exponent = exponent + 1
        print(j)
printPowersOfTwo()

print("====================================================")
#Program 2: SecondLoop
#write a loop statement that computes:
# A- The sum of all even numbers between 2 and 200(inclusive).
#Note: Use function called sumOfEvenNumbers to perform this loop.

def sumOfEvenNumbers():
    sum = 0
    counter = 2
    for m in range(counter, 201 ):
        if m %2 == 0:
            sum +=m
        m += 1
    print(sum)
sumOfEvenNumbers()

#B - The sum of all squares between 1 and 200(inclusive). Use function called sunOfSquares to perform this loop.
print("====================================================")

def sumOfEvenNumber():
    sum = 0
    counter = 1
    for j in range(counter,201):
        sum += j ** 2
        j += 1
    print(sum)
sumOfEvenNumber()

print("====================================================")

#Program 3: ThirdLoop
#write program that read a sequence of interger inputs and print:
# A - The smallest and largest of the inputs


print("====================================================")

numberSet = str(input("Enter your numbers: "))
number = ""
evenNumbers = ""
oddNumbers = ""
for i in numberSet:
    number = number + "" + i
    i = int(i)
    i +=1
print(f"The smallest number is {min(number)} and the largest number is {max(number)}")

# B - The number of even inputs.
print("====================================================")

numSet = str(input("Enter your numbers: "))
for e in numSet:
    e = int(e)
    if e %2 == 0:
        evenNumbers = evenNumbers + "" + str(e)
        e += 1
print(f"The count of even numbers is {len(evenNumbers)}")
