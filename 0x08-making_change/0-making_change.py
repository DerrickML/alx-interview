#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.

    Dyanimc Programmming Bottom Up Solution
    """
    if total <= 0:
        return 0
    # initialize list with maximum amount(which cannot be reached)
    # this helps to calculate a new minimum
    # e.g if total = 2, list = [3,3,3]
    dp = [total + 1] * (total + 1)
    # set minimum number of coins for amount 0
    dp[0] = 0

    # start from 1 because we know dp[0]
    for amount in range(1, total + 1):
        # test for every coin
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[total] if dp[total] != total + 1 else -1
