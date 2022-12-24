#!/usr/bin/python3
"""
Module 0-island_perimeter
"""


def island_perimeter(grid):
    """
    Determines the perimeter of
    an island
    """
    visited = set()

    if not grid:
        return 0

    def dfs(i, j):
        """depth first search"""
        if (i, j) in visited:
            return 0
        if i >= len(grid) or\
                j >= len(grid[0]) or\
                i < 0 or j < 0 or\
                grid[i][j] == 0:
            return 1
        visited.add((i, j))
        result = dfs(i, j + 1)
        result += dfs(i, j - 1)
        result += dfs(i + 1, j)
        result += dfs(i - 1, j)
        return result

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # do a dfs for only land
            if grid[i][j]:
                return dfs(i, j)
    return 0
