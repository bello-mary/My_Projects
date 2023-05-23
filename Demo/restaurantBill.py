"""
Assign a float value to variable
Assign a value for originalBill
Assign a value for variableTax
Assign a value for variableTip
Assign a value for variableTotal 
"""


def main():

    #input
    print("your original bill")
    originalBill = float(85) 

    #originalBill = float(input("please enter your original Bill amount "))
    variableTax  = float(.15 * originalBill)
    variableTip = float(.20 * originalBill)
    
    #processing
    totalBill = originalBill + variableTax + variableTip

    #output
    print("your original Bill amount is: ", originalBill)
    print("your Tax is : " , variableTax)
    print("your tip is : " , variableTip)
    print("your total Bill is : " , totalBill)
if __name__ == "__main__":
        main()

    
