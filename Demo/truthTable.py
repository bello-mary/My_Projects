def main():
    #Input
    stMark = float(input("Enter the student's mark : "))

    #Processing
    if stMark >=90 and stMark <=100:
        print("Excellent !!!!")
        
    elif stMark >=80 and stMark <90:
        print("Very Good")
    
    if stMark >=90:
        if stMark <=100:
        
            print("Excellent !!!!")   
    else :
        print("The mark is not validated")       


main()