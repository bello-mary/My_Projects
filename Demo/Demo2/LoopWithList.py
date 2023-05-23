# Index     0         1       3
stNames =["Yousef", "Brad", "Geoff"]
stGrades = [55, 95,99]
print(stNames)
print(stGrades)

# Out of range at stNames[3]]
# for i in range(3):
#     print(stNames[i])

print("Total elements in stName list :" , len(stNames))
for i in range(len(stNames)):
    print(stNames[i])

print("stName          stGrades")
print("------------------------")
for i in range(len(stNames)):
    print(stNames[i], "  " ,stGrades[i])

#Foreach loop : Usually used with list

for element in stNames: 
    print(element)
print("----------------------------------")

for stNames in stNames: 
    print(stNames)

print("-----------------------------------")
for stGrades in stGrades: 
    print(stGrades)

