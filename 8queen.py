def is_safe(board, row, col):
    for i in range(col):
        if (board[row][i] or 
            any(board[r][c] for r, c in zip(range(row, -1, -1), range(col, -1, -1))) or 
            any(board[r][c] for r, c in zip(range(row, len(board)), range(col, -1, -1)))):
            return False
    return True

def solve(board, col=0):
    if col == len(board): return True
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, col + 1): return True
            board[row][col] = 0
    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))

n = 8
board = [[0] * n for _ in range(n)]
if solve(board): print_solution(board)
else: print("No solution.")
