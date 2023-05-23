sum = 0 #initializing the value of sum

# for counter in range(10): #initial value of counter is 0. 
#     #we have the logical condition to keep performing the loop(keep interating) >>>> if counter <10
#     sum = sum + counter
#     print("counter = ", counter)
# print("The total sum is : ", sum)


sum = 0
for counter in range(2, 20, 3): #initial value of counter is 0. 
    #we have the logical condition to keep performing 
    # the loop(keep interating) >>>> if counter <20
    # the counter value will be increased by 3 for each interation
    sum = sum + counter
    print("counter = ", counter)
print("The total sum is : ", sum)

sum = 0
for counter in range(20, 2, -2): #initial value of counter is 20. 
    #we have the logical condition to keep performing 
    # the loop(keep interating) >>>> if counter >2
    # the counter value will be increased by 3 for each interation
    sum = sum + counter
    print("counter = ", counter)
print("The total sum is : ", sum)