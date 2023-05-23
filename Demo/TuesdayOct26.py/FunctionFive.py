def calculateTax(price, taxrate):
    result = price * taxrate
    return result


productPrice = float(input("Enter the product price"))
theTaxRate = float(input("Enter the taxrate"))
totalPrice = calculateTax(productPrice, theTaxRate)
print("The Product's price after tax is {0:.2f}".format(totalPrice))

productPrice = float(input("Enter the product price"))
theTax = float(input("Enter the taxrate"))
totalPrice = calculateTax(productPrice, theTax)
print("The Product's price after tax is {0:.2f}".format(totalPrice))

productPrice = float(input("Enter the product price"))
theTax = float(input("Enter the taxrate"))
totalPrice = calculateTax(productPrice, theTax)
print("The Product's price after tax is {0:.2f}".format(totalPrice))
