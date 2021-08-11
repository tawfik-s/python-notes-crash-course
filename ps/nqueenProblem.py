board=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]


N=len(board)

def isSafe(board,row,col):
    #Check this row on left side
    for i in range(col):
        if board[row][i]==1:
            return False
    
    #check upper diagonal on left side
    for i, j in zip(range(row,-1,-1),
                    range(col,-1,-1)):        
        if board[i][j]==1:
            return False

    #check lower diagonal on left side
    for i,j in  zip(range(row,N,1),
                     range(col,-1,-1)):
        if board[i][j]==1:
            return False
    
    return True


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

def solveNquetil(board,col):

    #base case
    if col >= N:
        return True
    
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1

            if solveNquetil(board,col+1):
                return True

            board[i][col]=0

    return False




def solveNQeen():
    if not solveNquetil(board,0):
        print("solution does not exist")

    printSolution(board)


solveNQeen()












