#!/usr/bin/python3
"""A Program that solves N QUeeen puzzle"""

import sys


def solve_nqueens(n: int) -> list:
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n (int): The number of queens and the size of the chessboard.

    Returns:
        list: A list of all possible solutions. Each solution is represented
        as a list of integers,
              where the value of i-th integer represents the column number of
              the queen in the i-th row.
    """
    def is_attack(i: int, j: int) -> bool:
        """
        Check if placing a queen at cell (i, j) will be safe.

        Args:
            i (int): The row number.
            j (int): The column number.

        Returns:
            bool: True if it's safe to place a queen at cell (i, j),
            False otherwise.
        """
        for k in range(i):
            if board[k] == j or board[k] - k == j - i or board[k] + k == j + i:
                return True
        return False

    def place_queen(i: int, n: int) -> None:
        """
        Place queens on the chessboard using backtracking.

        Args:
            i (int): The current row number.
            n (int): The number of queens and the size of the chessboard.
        """
        if i == n:
            result.append(board[:])
            return
        for j in range(n):
            if not is_attack(i, j):
                board[i] = j
                place_queen(i + 1, n)

    result = []
    board = [-1] * n
    place_queen(0, n)
    return result


def print_result(result: list) -> None:
    """
    Print all solutions to the N-Queens problem in a specific format.

    Args:
        result (list): A list of all solutions to the N-Queens problem.
    """
    for res in result:
        print([[i, res[i]] for i in range(len(res))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

print_result(solve_nqueens(n))
