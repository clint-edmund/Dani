def perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        float: The calculated perimeter of the rectangle.
    """
    # Calculate the perimeter using the formula 2 * (length + width)
    perimeter_result = 2 * (length + width)
    
    # Return the calculated perimeter
    return perimeter_result

# Example usage:
length = 20
width = 7
print("Perimeter:", perimeter(length, width))