#!/usr/bin/python3
"""UFT-8 Encoding"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Check if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    count = 0  # Initialize a variable to keep track of the number of bytes
    # remaining for the current character

    for num in data:
        if count == 0:
            # Determine the number of bytes required for the current character
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                # If the 8th bit is set, it's not a valid start of a character
                return False
        else:
            # For continuation bytes, the 2nd highest bit should be '10'
            if (num >> 6) != 0b10:
                return False
            count -= 1  # Decrement the count of remaining bytes for
            # the current character

    return count == 0  # All characters are valid if count is back to 0
