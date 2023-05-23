countryName = input("Enter the country's name : ")

totalOrder = float(input("What is your order ? "))

def main():
    if countryName.lower() == "canada" : 
        calOrderWhenCanada()
    else:
        calWhenNotCanada()

def calOrderWhenCanada():
    
    provinceName = input("Enter the province name : " )
    if provinceName.lower() == "Alberta" :
        taxAmount = 0.05 * totalOrder

    elif provinceName.lower() == "Ontario" or provinceName.lower() == "Nova Scotia" or provinceName.lower() == "New Brunswick" :
        taxAmount = 0.15 * totalOrder

    else:
        taxAmount = 0.11 * totalOrder

    totalOrderWithTax = taxAmount + totalOrder 
    print("Because you entered Canada, your total is : $", totalOrderWithTax)
    print(totalOrderWithTax)

def calWhenNotCanada(): 
    taxAmount = 0

    totalOrderWithoutTax = taxAmount + totalOrder
    print(totalOrderWithoutTax) 

main()