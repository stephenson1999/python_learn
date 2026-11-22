
# 8 Queens Problem using Backtracking

N = 8
board = [-1] * N


# Part 1: Check if a queen is safe
def is_safe(board, row, col):
    for r in range(row):
        c = board[r]

        # Check same column
        if c == col:
            return False

        # Check diagonals
        if abs(r - row) == abs(c - col):
            return False

    return True


# Part 2: Solve using backtracking
def solve(board, row):
    # All 8 queens have been placed
    if row == N:
        return True

    # Try every column in this row
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col

            # Try placing the next queen
            if solve(board, row + 1):
                return True

            # Backtrack if it doesn't work
            board[row] = -1

    return False


# Part 3: Print the chessboard
def print_board(board):
    for col in board:
        for j in range(N):
            if j == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Part 4: Run the program
if solve(board, 0):
    print("Solution found!")
    print_board(board)
else:
    print("No solution found.")
