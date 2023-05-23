def calculateTax(price):
    result = price * 1.15
    return result


productOnePrice = float(input("Enter the product price"))
productOnePriceWithTax = productOnePrice * 1.15
print("The total price is {0:.2f}".format (productOnePriceWithTax))


productTwoPrice = float(input("Enter product Two price"))
productTwoPriceWithTax = productTwoPrice * 1.15
print("The total price is {0:.2f}".format (productTwoPriceWithTax))


productThreePrice = float(input("Enter product Three price"))
productThreePriceWithTax = productThreePrice * 1.15
print("The total price is {0:.2f}".format (productThreePriceWithTax))

