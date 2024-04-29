def area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.
    """
    # Calculate the area by multiplying length by width
    return length * width

def perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated perimeter of the rectangle.
    """
    # Calculate the perimeter using the formula 2 * (length + width)
    return 2 * (length + width)

def main():
    # Prompt the user to input the length and width of a rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area and perimeter
    rectangle_area = area(length, width)
    rectangle_perimeter = perimeter(length, width)
    
    # Print the calculated area and perimeter with descriptive messages
    print("The area of the rectangle is:", rectangle_area)
    print("The perimeter of the rectangle is:", rectangle_perimeter)

# Call the main function to execute the program
main()
