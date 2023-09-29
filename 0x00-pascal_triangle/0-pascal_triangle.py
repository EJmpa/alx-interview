#!/usr/bin/python3
"""A function that returns list of integers containing pascal's triangle of `n`"""
def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []  # Return an empty list for invalid input.

    triangle = [[1]]  # Initialize Pascal's Triangle with the first row, which contains a single 1.

    for i in range(1, n):
        prev_row = triangle[i - 1]  # Get the previous row in the triangle.
        new_row = [1]  # Initialize a new row with 1 at the beginning.

        for j in range(1, i):
            # Calculate and append the middle elements of the row.
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Add 1 to the end of the new row.
        triangle.append(new_row)  # Append the new row to the triangle.

    return triangle
