# This program will calculate the length and height of two rectangles and compare the area of each rectangle

lengthOne = int(input("\nWhat's the length of Rectangle 1? "))
heightOne = int(input("\nWhat is the height of Rectangle 1? "))
areaOne = heightOne * lengthOne
print("The area for Rectangle 1 is", areaOne)

lengthTwo = int(input("\nWhat's the length of Rectangle 2? "))
heightTwo = int(input("\nWhat's the height of Rectangle 2? "))
areaTwo = lengthTwo * heightTwo
print("The area of Rectangle 2 is", areaTwo)
if areaOne == areaTwo:
    print("\nThe area of Rectangle 1 and Rectangle 2 are equal, both have length of", lengthOne,"and a height of", heightOne)
else:
    print("\nThey don't match")