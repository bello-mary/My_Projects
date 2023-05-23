 

#Input
houseNumber = int(input("Enter House Number : " ))
propertyDept = float(input("Enter property depth (feet) : " ))
propertyWidth = float(input("Enter property width (feet) : " ))
grassType = input("Enter type of grass (fescue, bentgrass, campus) : " )
numOfTrees = int(input("Enter the number of trees : " ))
labourCharge = 1000


#Process
totalArea = propertyDept * propertyWidth

#output
if totalArea >5000 :
    excessarea = 500
else:
    excessarea =0

if grassType.lower() == "fescue" :
    grasscost = 0.05
elif grassType.lower() == "bentgrass" :
    grasscost = 0.02
elif grassType.lower() == "campus" :
    grasscost = 0.01

costOfTrees = numOfTrees * 100


totalcost = costOfTrees + labourCharge + (totalArea * grasscost) + excessarea
print("Total cost for house", houseNumber, "is : ${0:.02f}".format(totalcost))


