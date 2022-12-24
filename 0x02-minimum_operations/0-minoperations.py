#!/usr/bin/python3
"""
Module 0x02-minimum_operations
"""


def minOperations(n: int) -> int:
    """
    Returns fewest number of operations
    needed to result in exaclty n H
    characters in the file
    """
    counter = 0

    if n <= 1:
        return counter

    for i in range(2, n + 1):
        while (0 == n % i):
            counter = counter + i
            n = n / i
            if n < i:
                break
    return counter
