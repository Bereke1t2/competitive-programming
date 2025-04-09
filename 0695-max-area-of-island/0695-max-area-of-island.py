class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[-1,0],[1,0],[0,1],[0,-1]]

        seen = set()
        row , col = len(grid) , len(grid[0])
        def inbound(i,j):return (0<=i<row and 0<=j<col)
        def dfs(i,j):
            Sum = 0
            if not inbound(i,j) or not grid[i][j] or (i,j) in seen:
                return Sum
            seen.add((i,j))
            for incx , incy in dir:
                Sum +=dfs(i+incx , j + incy)
            return Sum +1
        max_ = 0
        for i in range(row):
            for j in range(col):
                max_ = max(max_ , dfs(i,j))
        return max_


            