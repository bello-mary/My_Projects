# Name: Mary Bello
# W Number: W0451351
# Assignment: Erewhon Mobile Data Plans.

#Input
totalDataUseage = float(input("Enter data usage (Mb) : " ))

#Process
if totalDataUseage <= 200 :
    totalCharge = float(20)

else:
    if totalDataUseage >200 and totalDataUseage <=500 :
        totalCharge = 0.105 * totalDataUseage
    elif totalDataUseage >500 and totalDataUseage <=1000 :
        totalCharge = 0.110 * totalDataUseage

  
print("Total charge is ", "${0:.02f}".format(totalCharge))