"""
Assign float value to purchasePrice
Assign float value to sellingPrice
Assign float value to percentagePrice
Print the the two value
precentageProfit = (((100 * (sellingPrice - purchasePrice)/ purchasePrice))
Print(percentageProfit)
"""

def main():

    #Input
    print("percentageProfit")
    purchasePrice = 10.0
    sellingPrice = 15.0
    
    #processing
    percentageProfit = 100 *(sellingPrice - purchasePrice)/purchasePrice


    #output
    print("you entered")
    print(sellingPrice)
    print(purchasePrice)
    print("the percentageProfit: " + str("{:.2f}".format(percentageProfit)) + "%")

if __name__ == "__main__":
    main()