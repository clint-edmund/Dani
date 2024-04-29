# What are the dimensions of the first rectangle
lengthOne = float(input("Enter the length of the first rectangle: "))
heightOne = float(input("Enter the height of the first rectangle: "))

# What are the dimensions of the second rectangle
lengthTwo = float(input("Enter the length of the second rectangle: "))
heightTwo = float(input("Enter the height of the second rectangle: "))

# Calculate the areas of the rectangles
areaOne = lengthOne * heightOne
areaTwo = lengthTwo * heightTwo

# Compare the areas and print to screen
if areaOne > areaTwo:
    print("Rectangle 1 has a larger area:")
    print("Area:", areaOne)
    print("Length:", lengthOne)
    print("Height:", heightOne)
elif areaTwo > areaOne:
    print("Rectangle 2 has a larger area:")
    print("Area:", areaTwo)
    print("Length:", lengthOne)
    print("Height:", heightTwo)
else:
    print("Both rectangles have equal areas:")
    print("Area:", areaOne)
    print("Length of Rectangle 1:", lengthOne)
    print("Height of Rectangle 1:", heightOne)
    print("Length of Rectangle 2:", lengthTwo)
    print("Height of Rectangle 2:", heightTwo)
