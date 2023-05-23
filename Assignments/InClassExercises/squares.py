# n = int(input("Enter the value of n : "))
# counter = 0
# while counter ** 2 < n :
#     print(counter ** 2)
#     counter +=1 

print("continue part")
# continue & Break
evenNumbers = 0
for i in range(20):
    if i  == 5:
        continue # Go back to the next new iteration
        # skip the remaining statement inside the loop
    if i == 8:
        continue
    if i == 14:
        break # exit loop
    print(i)
    
    if (i %2 == 0):
        print("{0} is even number".format(i))
        evenNumbers +=1
    else:
        print("{0} is an odd number".format(i))

print("Done")






