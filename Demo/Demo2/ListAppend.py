
#Index       0        1       2
stNames =["Yousef", "Brad", "Geoff"]
stGrades = [55, 95,-20,-100, 130, 105, 112]

mixList = ["Yousef", 77, "Brad", 90] # not preferable
print(mixList)

print(stNames)


print("-------------------------------------------------")
stNames.append("Eli")
print(stNames)

print("-------------------------------------")
stNames.append("Hello")
print(stNames)

print("-------------------------------------")
stNames.remove("Hello")
print(stNames)

print("-------------------------------------")
stNames.insert(1,"Hello")
print(stNames)
print("-------------------------------------")
for i in range(len(stNames)):
    print(stNames[i])

#remove the student name of index 1
print("-------------------------------------")
stNames.remove(stNames[1])
print(stNames)

#change the a name
print("-------------------------------------")
for i in range(len(stNames)):
    if stNames[i] == "Yousef":
        stNames[i] = "Yousef Abu Baker"
print(stNames)


print("-------------------------------------")
print(stGrades)
for i in range(len(stGrades)):
    if stGrades[i] < 0: #if negative value change it to 0
        stGrades[i] = 0
print(stGrades)


print("-------------------------------------")
print(stGrades)
for i in range(len(stGrades)):
    if stGrades[i] > 100: #if negative value change it to 0
        stGrades[i] = 100
print(stGrades)