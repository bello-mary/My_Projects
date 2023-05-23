"""
Declare the variable balance as type Float
Assign the value 100 to the variable balance 
Increase variable balance by 5% of its value, and add 100
Increase the variable balance by 5% of its value, and add 100
Increase the variable balance by 5% of its value
display the variable balance (rounded to two decimal places) in the console window
"""

def main():

    #Input
    print("savingAccount")
    deposit = 100.0

    #processing
    variableBalance = (((deposit * 1.05 + 100) * 1.05 + 100) * 1.05)

    #output
    print("you entered")
    print(deposit)
    print("Ths variableBalance is : {0:.2f} for the previous variableBance".format(variableBalance))


main()