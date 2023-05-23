def main():
    #Input
    stMark = float(input("Enter the student's mark : "))

    #Processing
    if stMark > stMark <0 : # Input Validation   
            print("Invalid student's mark ")
    else:
        if stMark >=90 and stMark <=100:
            print("Excellent")
        elif stMark >=80 and stMark <=90:
            print("Very Good !!!!")   
        elif stMark >70 and stMark <80:
            print("Good")
        elif stMark >=60 and stMark <70:
            print("pass")        



main()