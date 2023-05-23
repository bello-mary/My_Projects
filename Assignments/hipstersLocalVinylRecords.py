def main():

    #Input
    
    print("Hisper's Local Vinyl Records - Customer Order Details" )

    customerName = input("Enter customer's name : " )
    distance = float(input("Enter the distance in kilometers for delivery : " ))
    recordsCost = float(input("Enter the cost of records purchased : " ))
    


    #Processing
    
    print("Purchase summary for" , customerName)
    deliveryCost = distance * 15
    purchaseCost = recordsCost * 1.14
    totalCost = deliveryCost + purchaseCost
 

    #Output
    print("Delivery Cost:", "${:.2f}".format(deliveryCost))
    print("Purchase Cost:", "${:.2f}".format(purchaseCost))
    print("Total Cost   :", "${:.2f}".format(totalCost))

main() 