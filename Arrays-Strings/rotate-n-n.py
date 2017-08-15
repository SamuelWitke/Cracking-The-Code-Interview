#Python 3 only
def print_grid(grid):
    for row in grid:
        for e in row:
            print(e,end='')
        print()

def rotate(grid):
    n = len(grid)
    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(last):
            offset = i - first
            top = grid[first][i]
            #left -> top
            grid[first][i] = grid[last-offset][first]
            #bottom -> right
            grid[last-offset][first] = grid[last][last-offset]
            #right -> bottom
            grid[last][last-offset] = grid[i][last]
            #top -> right
            grid[i][last] = top
    return grid

arr = []
arr.append(input().split())
for x in range(len(arr[0]) - 1):
    arr.append(input().split())
print_grid(arr)
arr = rotate(arr)
print()
print_grid(arr)
