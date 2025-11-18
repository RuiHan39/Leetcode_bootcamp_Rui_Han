from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshorange = []
        r = len(grid)
        c = len(grid[0])
        rottenqueue = deque([])
        time = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    freshorange.append((i,j))
                if grid[i][j] == 2:
                    rottenqueue.append((i,j))
        freshorangeset = set(freshorange)

        lenroq = len(rottenqueue)
        while rottenqueue and freshorangeset:
            time += 1
            for _ in range(lenroq):
                row,col = rottenqueue.popleft()
                if row-1 >=0 and grid[row-1][col] == 1:
                    rottenqueue.append((row-1,col))
                    grid[row-1][col] = 0
                    freshorangeset = freshorangeset - set([(row-1,col)])
                if row+1 < r and grid[row+1][col] == 1:
                    rottenqueue.append((row+1,col))
                    grid[row+1][col] = 0
                    freshorangeset = freshorangeset - set([(row+1,col)])
                if col-1 >=0 and grid[row][col-1] == 1:
                    rottenqueue.append((row,col-1))
                    grid[row][col-1] = 0
                    freshorangeset = freshorangeset - set([(row,col-1)])
                if col+1 < c and grid[row][col+1] == 1:
                    rottenqueue.append((row,col+1))
                    grid[row][col+1] = 0
                    freshorangeset = freshorangeset - set([(row,col+1)])
            lenroq = len(rottenqueue)
        if not freshorangeset:
            return time
        else:
            return -1




