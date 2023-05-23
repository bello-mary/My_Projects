stNames = []

for i in range(4):
    stName = input("Enter the student name   :  ") # stName is another variable, different from stNames.
    stNames.append(stName) # append the variable stName
print(stNames)

print("======================================")
#not prefered
stNames.append("Yousef")
stNames.append("Abel")
stNames.append("Grace")
stNames.append("Suzy")
stNames.append("Eli")
stNames.append("Anne")
stNames.append("Bill")
print(stNames)

print("============================================================")

# # for assignment 3

nValue = [10,4,7,1000,-9]
print(max(nValue))
print(min(nValue))


print("============================================================")
# for i in range(5):
#     n = int(input("Enter the value of n : "))
#     if 

print("============================================================")

nValue = [10,4,7,100,100,100]
print("The maximun value is : ", max(nValue))
print("The minimum value is : ", min(nValue))
print("The total count of 100 is : ", nValue.count(100))


