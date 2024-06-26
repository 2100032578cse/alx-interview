#!/usr/bin/python3
"""
0-pascal_triangle.py
"""

def pascal_triangle(n):
    """
    Returns the list of lists of integers representing the Pascal’s triangle of n.
    """
    if n <= 0:
        """Return an empty list if n is less than or equal to 0"""
        return [] 

    triangle = []
    for i in range(n):
        """Initialize the row with ones (1s)"""
        row = [1] * (i + 1)
        for j in range(1, i):
            """Calculate the value based on the previous row"""
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        """Add the row to the triangle"""

        triangle.append(row)
    
    """Return the complete Pascal's triangle"""
    return triangle
