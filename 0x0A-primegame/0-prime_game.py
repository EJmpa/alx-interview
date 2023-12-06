#!/usr/bin/python3
"""
Prime Game

This module contains a function that determines the winner of the Prime Game.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Parameters:
    x (int): The number of rounds.
    nums (list of int): The maximum number for each round.

    Returns:
    str: The name of the player that won the most rounds,
    or None if there is a tie.
    """
    # Check if nums is empty or x is less than 1
    if not nums or x < 1:
        return None

    # Find the maximum number in nums
    n = max(nums)

    # Generate a list of prime numbers up to n
    prime = [0, 0] + [1] * (n - 1)
    for i in range(int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = 0

    # Count the cumulative number of primes
    prime_count = [0] * (n+1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i-1] + prime[i]

    # Determine the winner of each round
    player1 = 0
    for n in nums:
        player1 += prime_count[n] % 2 == 1

    # Determine the overall winner
    if player1 * 2 == x:
        return None
    if player1 * 2 > x:
        return "Maria"
    return "Ben"
