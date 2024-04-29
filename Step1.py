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
    area_result = length * width
    
    # Return the calculated area
    return area_result

# Example usage:
length = 16
width = 8
print("Area:", area(length, width))
