from numpy import matrix
def GetPath(maze):
    if(maze == None or maze.size == 0):
        return None
    path = []
    if(getPath(maze,1,1,path)):
        return path
    return None
def getPath(maze,row,col,path):
    if(col < 0 or row < 0 or not maze[row][col]):
        return false
    isAtOrigin = (row == 0) and (col == 0)
    if( isAtOrigin or getPath(maze,row,col-1,path) or getPath(maze,row -1, col,path)) :
        p = [row,col]
        print(p)
        path.add(p)
        return true
    return false
A = matrix([[True,True,True],
           [False,True,True],
           [True,False,True]])
print(A[0][0][0])
print(GetPath(A))
