def printSolution(board):
    for i in range(n):
        for j in range(n):
            if board [i][j] == 1 :
                print("Q", end = " ")
            else:
                print(".", end = " ")
        print()
        
def solveNqueen(board, col):
    if col == n :
        return True
    for i in range(n):
        if isSafe(board, i, col):
            board [i][col] = 1
            if solveNqueen(board, col + 1):
                return True
            board [i][col] = 0
    return False
    
def isSafe(board, row, col):
    for x in range(col):
        if board [row][x] == 1 :
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board [x][y] == 1 :
            return False
    for x, y in zip(range(row, n, 1), range(col, -1, -1)):
        if board [x][y] == 1 :
            return False
    return True

import time
n = int(input("Enter the size of the N-Queen board: "))
if n <= 3 :
    print("No Solution exits for n < 4.")
else:
    start = time.time()
    board = [[0 for x in range(n)] for y in range(n)]
    print("Original board is : ")
    for i in range(n):
        for j in range(n):
            print(".", end=" ")
        print()
    if not solveNqueen(board, 0):
        print("No solution found")
    print("Solution board is : ")
    printSolution(board)
    end = time.time()
    total = end - start
    print("Total time taken : ", total, "ms")