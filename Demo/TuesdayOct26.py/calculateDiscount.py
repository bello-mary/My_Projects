def calculateTax(price, taxrate):
    result = price * taxrate
    return result

def afterDiscount(totalPrice):
    discount = 0
    if totalPrice >=500:
        discount = 100
    return totalPrice - discount 



productPrice = float(input("Enter the product price"))
theTaxRate = float(input("Enter the taxrate"))
totalPrice = calculateTax(productPrice, theTaxRate)

print("The Product's price after tax is {0:.2f}".format(totalPrice))

theDiscountAmount = afterDiscount(totalPrice)

print("The total price after discount is {0:.2f}".format(theDiscountAmount))

