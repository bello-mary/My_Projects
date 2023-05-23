"""
Name: Mary Bello
Student ID: W0451351

"""
#Find the sum of odd and even number between -1 and -200

sumOfEvenNum = 0
sumOfOddNum = 0
for g in range(-1,-200):
    if g %2 != 0:
        sumOfOddNum = sumOfOddNum + g
        g += 1
    else:
        sumOfEvenNum = sumOfEvenNum + g
        g += 1
print("The sum of all odd number is :" , sumOfOddNum)
print("The sum of all even number is :" , sumOfEvenNum)