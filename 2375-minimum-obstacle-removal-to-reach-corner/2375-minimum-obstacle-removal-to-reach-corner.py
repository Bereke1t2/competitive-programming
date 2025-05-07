class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        min_heap = [(grid[0][0], 0 , 0)]
        seen = [[False] * m for _ in range(n)]
        def inbound(x ,y):
            nonlocal n , m 
            return 0<= x <n and 0<=y<m
        dirn = [[-1,0] , [0,-1],[0,1] , [1,0]]
        while min_heap:
            min_ , row , col = heappop(min_heap)
            if seen[row][col]:continue
            if (row, col) == (n-1 ,m -1):
                return min_
            seen[row][col] = True
            
            for dx , dy in dirn:
                x, y = row + dx , col + dy 
                if not inbound(x, y) or seen[x][y]:continue
                heappush(min_heap , (min_ + grid[x][y] , x , y))
