#!/usr/bin/python3
"""UTF-8 Encoding"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determine if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Initialize a variable to count the number of
    # bytes for the current character
    num_bytes = 0

    for byte in data:
        # Check if the 8th bit is set (i.e., if it's not in the range [0, 127])
        if byte >= 128:
            # Check if it's a continuation byte (binary: 10xxxxxx)
            if num_bytes == 0:
                return False

            # Decrement the count of remaining bytes
            num_bytes -= 1
        else:
            # Determine the number of bytes required for the current character
            if num_bytes > 0:
                return False
            if byte < 128:
                num_bytes = 0
            elif byte < 192:  # Binary: 110xxxxx
                num_bytes = 1
            elif byte < 224:  # Binary: 1110xxxx
                num_bytes = 2
            elif byte < 240:  # Binary: 11110xxx
                num_bytes = 3
            else:
                return False

    # Check if all characters are properly terminated
    return num_bytes == 0
