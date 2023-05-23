def Main():
    #Input
    gpaValue = int(input("Enter the gpaValue : "))

    #Processing & Output
    if gpaValue == 4:
         print("Your garde is A")
    
    elif gpaValue == 3:
        print("Your garde is B")
    elif gpaValue == 2:
         print("Your garde is c")
    elif gpaValue == 1:
        print("Your Grade is D")
    else : 
        print("Incorrect GPA value. Try again later")
    
Main()