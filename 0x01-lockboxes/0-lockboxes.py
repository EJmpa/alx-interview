#!/usr/bin/python3
"""A functon that checks if all boxes can be opened"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened using BFS traversal.

    Args:
        boxes (list of lists): A list of lists representing locked boxes and
        their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Create a set to keep track of the keys we have.
    keys = set([0])

    # Create a queue for BFS traversal, starting from the first box (box 0).
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        # Iterate through the keys in the current box.
        for key in boxes[current_box]:
            # If we find a new key and it corresponds to a valid box number,
            # add it to our set of keys and queue.
            if key not in keys and key < len(boxes):
                keys.add(key)
                queue.append(key)

    # If all boxes have been visited (all keys have been found), return True.
    return len(keys) == len(boxes)
