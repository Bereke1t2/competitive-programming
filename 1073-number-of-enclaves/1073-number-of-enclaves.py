class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows , cols  = len(grid) , len(grid[0])
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        def dfs(i,j):
            if not is_inbound(i,j) or grid[i][j]==0:
                return 0 
            grid[i][j] = 0
            count = 0
            for dx , dy in directions_straight:
                count +=dfs(i+dx,j+dy)
            return count +1
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and  i==0 or j == 0 or i == rows -1 or j == cols -1:dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    count +=dfs(i,j)
        return count

                    