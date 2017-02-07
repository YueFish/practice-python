

#coding:utf-8
grid=[
[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
[1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def valid(grid,x,y):
    if x >= 0 and x < len(grid) and y>=0 and y < len(grid[0])and grid[x][y] == 1:
        return True
    else:
        return False
def walk(grid,x,y):
    if x == len(grid)-1 and y ==len(grid[0])-1:
        print("get out")
        grid[x][y]=2
        return True
    if valid(grid,x,y):
        grid[x][y]=2
        if walk(grid,x,y+1) or walk(grid, x-1, y) or walk(grid, x, y-1) or walk(grid, x+1, y):
            return True
        else:
            grid[x][y] =1
            return False
    else:
        return False

if __name__ =='__main__':
    walk(grid,0,0)
    for i in range(len(grid)):
        print(grid[i])