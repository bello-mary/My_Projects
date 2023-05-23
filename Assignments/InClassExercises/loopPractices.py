"""
Name: Mary Bello
Student ID: W0451351.
Loop Practices

"""
# Write a loop that prints
# question 1

# n = 0
# while n < 100:
#     print(n **2)
#     n+=1

# counter = 1
# n = 100 # int(input())
# Square = counter **2
# while Square <n:
#     print(Square)
#     counter +=1
#     Square = counter**2

# n= 100 #int(input())
# for counter in range(1,n):
#     square = counter*counter
#     if square>=n:break
#     print(square)

# All positive numbers that are divisible by 10 and less than n. example, 
# if n is 100, print 10 20 30 40 50 60 70 80 90

# factors = []
# num = 1
# while num <=100:
#     if num % 10 == 0:
#         factors.append(num)
#     num += 1
# print(factors) 

#=================== without list==============
# num = 1
# while num <=100:
#     if num % 10 == 0:
#         print(num)
#     num += 1

#===============concatination=================
num = 1
output = ""
while num <=100:
    if num % 10 == 0:
        output += str(num) + " , "
        #print(num)
    num += 1
print(output)


# All powers of two less than n. for example, if n is 100,
# print 1 2 4 8 16 32 64.

# n = 2
# exponent = 0
# while exponent < 7:
#     j = n ** exponent
#     exponent = exponent + 1
#     print(j)

#Write a loop that computes.



