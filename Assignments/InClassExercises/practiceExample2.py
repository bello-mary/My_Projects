"""
Name: Mary Bello
Student ID: W0451351

"""
# rewrite the following for loop as a while loop
# s = 0
# for i in range(1,10):
#     s = s + i
# print(s)

# s = 0
# i = 1
# while i <10:
#     s += i #s = s + i
#     i += 1 #increment until condition is false
# print(s)

#write programs that read sequence of interger input and print:

# the smallest and largest of the inputs.
number = str(input("Enter your numbers: "))
t = ""
evenNumbers = ""
oddNumbers = ""
for i in number:
    t = t + "" + i
    i = int(i)
    i +=1

#the number of even and odd inputs
# numSet = t
# for e in numSet:
#     e = int(e)
#     if e %2 == 0:
#         evenNumbers = evenNumbers + "" + str(e)
#         e += 1
#     else:
#         oddNumbers = oddNumbers + "" + str(e)
#         e += 1
# #cumulative totals. for example, if the inputs is 1 7 2 9, the program should print 1 8 10 19
# cumTotal = 0
# cumT = ""
# cumS = t
# for j in cumS:
#     j = int(j)
#     cumTotal += j
#     cumT = cumT + "  " + str(cumTotal)
#     j += 1



# print(f"The smallest number is {min(t)} and the largest number is {max(t)}")
# print(f"The count of even numbers is {len(evenNumbers)} and the count of odd number is {len(oddNumbers)}")
# print("The cummulative total is : ", cumT)





