#!/usr/bin/python3
"""A function that calculate minimum operations"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly 'n' H characters in the file.

    Args:
        n (int): The target number of H characters to achieve.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # Check if n is divisible by the current divisor
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1

    return operations
