countryName = input("Enter the country's name : ")

totalOrder = float(input("What is your order ? "))

if countryName.lower() == "canada" :
    provinceName = input("Enter the province name : " )

    if provinceName.lower() == "Alberta" :
        taxAmount = 0.05 * totalOrder

    elif provinceName.lower() == "Ontario" or provinceName.lower() == "Nova Scotia" or provinceName.lower() == "New Brunswick" :
        taxAmount = 0.15 * totalOrder

    else:
        taxAmount = 0.11 * totalOrder

else:
    taxAmount = 0

totalOrderWithTax = taxAmount + totalOrder
print(totalOrderWithTax)

# Calculate the total order including tax value and print it out to the console.
      