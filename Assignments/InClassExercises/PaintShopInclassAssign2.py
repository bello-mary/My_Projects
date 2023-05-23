"""
Student name: Mary Bello
Program Title: PaintShopAssignment_Inclass Assignment.
"""

lengthOfWall = int(input("enter the lengthOfWall value  "))
widthOfWall = int(input("enter the WidthOfWall value  "))
heightOfWall = int(input("enter the heightOfWall value  "))


def Main():
    calculateArea()

def calculateArea():
    Area = (widthOfWall*heightOfWall*2)*(lengthOfWall*heightOfWall*2) 
    numOfGallon =int((widthOfWall*heightOfWall*2)*(lengthOfWall*heightOfWall*2)/150)

    print("you entered")
    print("the length is : ", lengthOfWall)
    print("the width is : ", widthOfWall)
    print("the height is :" , heightOfWall)
    print("the area is : ", Area)
    print("your total number of gallon is: ",numOfGallon)

Main()