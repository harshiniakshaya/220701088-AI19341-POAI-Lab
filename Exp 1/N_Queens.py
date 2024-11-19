def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()


def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True
'''
zip([1, 2, 3], ['a', 'b', 'c'])
Result: [(1, 'a'), (2, 'b'), (3, 'c')]
'''

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return True  # Solution found, but continue to explore for multiple solutions

    has_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            has_solution |= solve_n_queens(board, row + 1, n)
            board[row][col] = False  # Backtrack

    return has_solution


def n_queens(n):
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")


# Test with 4 queens
n_queens(4)
'''
. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
'''
