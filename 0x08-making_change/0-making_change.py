#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    - coins (List[int]): a list of the values of the coins in your possession
    - total (int): the total to meet

    Returns:
    - int: fewest number of coins needed to meet total
    """

    # If total is less than or equal to 0, return 0
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)
    num_coins = 0

    # Iterate over each coin
    for coin in coins:
        # If total is 0, return the number of coins used so far
        if total == 0:
            return num_coins

        # Calculate how many of the current coin are needed to meet the total
        # (or as close as possible without going over)
        num_coins += total // coin

        # Reduce the total by the value of the coins used
        total %= coin

    # If total is not 0, it means the total cannot be met by any
    # number of coins you have, so return -1
    if total != 0:
        return -1

    # Return the number of coins used
    return num_coins
