class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def is_inbound(x, y):
            return 0 <= x < n and 0 <= y < n
        max_ = -1
        q = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j] = 1
                    
        level = 1
        while q:
            found = False
            for _ in range(len(q)):
                x , y = q.popleft()

                for dx ,dy in directions_straight:
                    nx, ny = x+dx , y +dy
                    if is_inbound(nx,ny) and grid[nx][ny]==0:
                        grid[nx][ny] = level
                        q.append((nx,ny))
                        found = True
            if found:
                max_ = max(max_ ,level)
            level +=1
        return max_