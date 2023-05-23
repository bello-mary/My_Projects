"""
Name: Mary Bello
Student ID: W0451351
"""
#Question 1.
#All squares less than n. For example, if n is 100, print 0 1 4 9 16 25 36 49 64 81
# n= 100 
# for counter in range(1,n):
#     square = counter*counter
#     if square>=n:break
#     print(square)

#Question 2.
# All positive numbers that are divisible by 10 and less than n. example, 
# if n is 100, print 10 20 30 40 50 60 70 80 90

# num = 1
# while num <=100:
#     if num % 10 == 0:
#         print(num)
#     num += 1

# All powers of two less than n. for example, if n is 100,
# print 1 2 4 8 16 32 64.

# n = 2
# exponent = 0
# while exponent < 7:
#     j = n ** exponent
#     exponent = exponent + 1
#     print(j)

# write a loop that computers
#the sum of all even numbers between 2 and 100 (inclusive)

# sum = 0
# counter = 2
# for m in range(counter, 101 ):
#     if m %2 == 0:
#         sum +=m
#     m += 1
# print(sum)

# the sum of all squares between 1 and 100 (inclusive)

# sum = 0
# counter = 1
# for j in range(counter,101):
#     sum += j ** 2
#     j += 1
# print(sum)

# #the sum of all odd numbers between a and b (inclusive)
# sum = 0
# a = 1
# b = 20
# for m in range(a, b ):
#     if m %2 != 0: # if m is divided by 2 and the reminder is not 0, then add that number (modulus does not show answer but show reminder)
#         sum +=m
#     m += 1
#     #print(sum)
# print(f"The sum is : {sum}.") 

#The sum of all odd digits of n. (For example, if n is 32677, the sum would be 3 + 7+7 =17.)
n = str(32677)
sum = 0
for k in n: # loop through the content of str n
    k = int(k) # every number inside string n convert it to int k and save it in k
    if k %2 != 0:
        sum += k
    k += 1
print(sum)