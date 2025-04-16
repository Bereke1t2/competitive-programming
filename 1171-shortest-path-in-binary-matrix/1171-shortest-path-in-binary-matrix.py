class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions_all = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows , cols = len(grid) ,  len(grid[0])
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        q = deque([(0,0,1)])
        if grid[0][0]:return -1
        grid[0][0] = 1
        while q:
            i , j , length = q.popleft()
            if (i,j)==(rows -1 , cols -1):
                return length
            for dx , dy in directions_all:
                x , y = i+dx , j + dy
                if is_inbound(x,y) and grid[x][y]==0:
                    grid[x][y] = 1
                    q.append((x,y,length +1))
        return -1
