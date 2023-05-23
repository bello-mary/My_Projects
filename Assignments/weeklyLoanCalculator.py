def main():

    #Input
    print("Weekly Loan Calculator")
    amountOfLoan = input("Enter the amount of Loan : ")
    interestRate = input("Enter the interest rate (%) : ")
    numberOfYears = input("Enter the number of years : ")

    #Processing
    #convert integer to float
    amountOfLoan = float(amountOfLoan)
    interestRate = float(interestRate)
    numberOfYears = float(numberOfYears)

    #calculate i using formular i = r/5200
    i = interestRate/5200

    #calculate weekly payment using the formular (i/(1 - (1 + i) ** (-52 * n))) * A
    #where A is the amount of loan and n is the number of years
    weeklyPayment = (i / ( 1 - ( 1 + i ) ** (-52 * numberOfYears ) ) ) * amountOfLoan
    weeklyPayment = round(weeklyPayment,2)

    #Output
    print("Your weekly payment will be:","${:,.2f}".format(weeklyPayment))










main()