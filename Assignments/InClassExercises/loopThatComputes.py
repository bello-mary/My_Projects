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

#the sum of all odd numbers between a and b (inclusive)
# sum = 0
# a = 1
# b = 20
# for m in range(a, b ):
#     if m %2 != 0: # if m is divided by 2 and the reminder is not 0, then add that number (modulus does not show answer but show reminder)
#         sum +=m
#     m += 1
#     #print(sum)
# print(f"The sum is : {sum}.") 

#indentation is important
# strictly equal to ==
# not equal to !=
#modulus % for even or odd numbers, if the modulus is strictly equal to 0 (== even) or if not equal to 0 (!= then its odd).

#The sum of all odd digits of n. (For example, if n is 32677, the sum would be 3 + 7+7 =17.)
n = str(1234567890)
sum = 0
for k in n: # loop through the content of str n
    k = int(k) # every number inside string n convert it to int k and save it in k
    if k %2 != 0:
        sum += k
    k += 1
print(sum)

