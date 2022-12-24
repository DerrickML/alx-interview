#!/usr/bin/python3
"""
Module 0-nqueens
A program that solves the N queens problem
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (num >= 4):
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """Solution for n queens"""
    col = set()  # keep track of used columns
    pos = set()  # (r + c) keep track of used positive diagonals
    neg = set()  # (r - c) keep track of used negative diagonals

    res = []  # final result

    board = [[] for n in range(n)]  # create empy board

    def backtrack(row):
        """function for recursion"""
        # means we've reached the last row
        if row == n:
            # get copy of current solution(current board)
            copy = board.copy()
            res.append(copy)
            return

        # for every column
        for c in range(n):
            # if we find that the column or diagonals are used, then skip
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            # register found columns and diagonals
            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            board[row] = [row, c]

            # move to next row
            backtrack(row + 1)

            # finally undo
            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            board[row] = []

    backtrack(0)

    return res


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)
