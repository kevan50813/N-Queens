
N = 8


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print("\n")


def safeMove(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    if col >= N:
        return True

    for i in range(N):
        if safeMove(board, i, col):
            board[i][col] = 1
            if solve(board, col+1):
                return True

            board[i][col] = 0

    return False


def NQueens():
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]
             ]

    if solve(board, 0) == False:
        print("No Solution Exsists")
        return False

    printSolution(board)
    return True


NQueens()
