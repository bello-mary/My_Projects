# varOne = random.randint(1,4)

#print(varOne)

stMark = float(input("Enter the student's mark : " ))

if stMark > 100 or stMark <0 : # In put Valdiation
    print("Invalid student's mark. Try again ")
else:
    if stMark >=90 and stMark <=100:
        print("Excellent")
    elif stMark >=80 and stMark <90:
        print("Very Good")
    elif stMark >=70 and stMark <80:
        print("Good")
    elif stMark >=60 and stMark <70:
        print("Pass")
    else:
        print("Fail")
    print("Folks, now you are qualified to start your 2nd Assignment")