class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:
        min_health = [(grid[0][0] ,0,0 )]
        n , m = len(grid) , len(grid[0])
        seen = [[False] * m for _ in range(n)]

        def inbound(x ,y):
            nonlocal n , m 
            return 0<= x <n and 0<=y<m
        dirn = [[-1,0] , [0,-1],[0,1] , [1,0]]
        if min_health[0][0]>=h:
            return False
        while min_health:
            health , row , col = heappop(min_health)
            if (row , col) == (n-1 , m-1):
                return True
            if seen[row][col]:continue
            seen[row][col] = True

            for dx  , dy in dirn:
                x , y = row +dx , col + dy
                if not inbound(x,y) or seen[x][y] or health + grid[x][y]==h:continue
                heappush(min_health , ( health + grid[x][y] , x,y))
        return False