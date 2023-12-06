#!/usr/bin/python3
"""
Determine the winner of the prime game for multiple rounds.
"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calculate_primes(n):
    """Calculate prime numbers up to n."""
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def isWinner(x, nums):
    """Determine the winner of the prime game for multiple rounds."""
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = calculate_primes(n)
        total_primes = len(primes)

        if total_primes % 2 == 0:
            # If the total number of primes is even, Ben wins
            wins["Ben"] += 1
        else:
            # If the total number of primes is odd, Maria wins
            wins["Maria"] += 1

    # Determine the overall winner
    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        # If the number of wins is equal, return None
        return None
