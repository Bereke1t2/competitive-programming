class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n , m = len(heights) , len(heights[0])
        min_heap = [(0 , 0 , 0)]
        seen = [[False] * m for _ in range(n)]

        def inbound(x ,y):
            nonlocal n , m 
            return 0<= x <n and 0<=y<m
        dirn = [[-1,0] , [0,-1],[0,1] , [1,0]]
        while min_heap:
            max_ , row , col = heappop(min_heap)
            if row==n-1 and col ==m-1:
                return max_
            if seen[row][col]:continue
            seen[row][col] = True
            
            h = heights[row][col]
            for dx , dy in dirn:
                x , y = row + dx , col + dy
                if not inbound(x , y) or seen[x][y]:continue
                h2 = heights[x][y]
                heappush(min_heap , (max(max_ , abs(h-h2)) , x , y))