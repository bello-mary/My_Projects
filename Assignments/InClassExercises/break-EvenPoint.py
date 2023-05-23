"""
Assign float value to fixedCost
Assign float value to pricePerUnit
Assign float value to costPerUnit
print the three numbers
breakEvenPoint = fixed cost / (pricePerUnit - costPerUnit)
print(break-EvenPoint)
"""

def main():

    print("breakEvenPoint")
    fixedCost = 5000.0
    pricePerUnit = 8.0
    costPerUnit = 6.0

    #processing
    breakEvenPoint = fixedCost / (pricePerUnit - costPerUnit)


    #output
    print("you entered")
    print(fixedCost)
    print(pricePerUnit)
    print(costPerUnit)

    print(breakEvenPoint)
    print("The Total value of breakEvenPoint " + str (breakEvenPoint))

main()