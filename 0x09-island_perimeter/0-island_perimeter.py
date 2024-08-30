#!/usr/bin/python3
"""
problem for island perimeter
"""


def island_perimeter(grid):
    """
    calculatinf the island parameter
    Args:
        grid: 2d list, 0(water), 1(land)
    return:
        island parameter
    """
    pr = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    pr += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    pr += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    pr += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    pr += 1
    return pr
