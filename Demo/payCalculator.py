def main():

    #Input
    print("Weekly payment calculator program")
    # Initialize numb er of variables
    overTimeHours = 0
    actualWorkingHours = 0
    hourlyPayRate = 0
    fixedWeeklyHours = 40

    actualWorkingHours = int(input("How many hours did you work this week : " ))
    hourlyPayRate = float(input("Enter the hourly rate : " ))

    #Processing
    totalWeeklyPayment = hourlyPayRate * actualWorkingHours

    if actualWorkingHours >= 40 :
        overTimeHours = actualWorkingHours - fixedWeeklyHours
        overTimePayment = overTimeHours * hourlyPayRate * 1.5
        totalWeeklyPayment = hourlyPayRate * fixedWeeklyHours + overTimePayment

    else :
         totalWeeklyPayment = hourlyPayRate * actualWorkingHours   
    #Output

    print("Your weekly payment is : ",totalWeeklyPayment)



main()