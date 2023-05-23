"""
Student name: Mary Bello
Program Title: PaintShopAssignment
Description:
Assign int value to lengthOfWall
Assign int value to widthOfWall
Assign int value to heightOfWall
print the three value OfWall
calculate the area of OfWall
calculate the numOfGallon

"""

def Main(): 

    #input
    print("welocome to our paintShopAssignment")
    lengthOfWall = int(input("enter the lengthOfWall value"))
    widthOfWall = int(input("enter the WidthOfWall value"))
    heightOfWall = int(input("enter the heightOfWall value"))


    #processing
    Area = (widthOfWall*heightOfWall*2)*(lengthOfWall*heightOfWall*2) 
    numOfGallon =(widthOfWall*heightOfWall*2)*(lengthOfWall*heightOfWall*2)/150 
    

    #output 
    print("you entered")
    print(lengthOfWall)
    print(widthOfWall)
    print(heightOfWall)
    print(Area)
    print("numOfGallon") = Area/150




Main
