

def printSolution(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print("\n")


def safeMove(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i in range(row):
        if board[col][i] == 1:
            return False
