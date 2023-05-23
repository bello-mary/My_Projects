def main():
    #Input
    stMark = float(input("Enter the student's mark : "))

    #Processing
    if stMark >=90:
        if stMark <=100:    
            print("Excellent !!!!")
            gpaValue = "A"
        else:
            print("The mark is not validated") 

    elif stMark >=80:
        if stMark <90:
            print("Very Good !!!!")   
    else :
        print("The mark is not validated")       


main()