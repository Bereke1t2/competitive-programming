class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(mat)  ,len(mat[0])
        ans = [[-1]*cols for _ in range(rows)]
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        q = deque()
        for i in range(rows):
            for j  in range(cols):
                if not mat[i][j]:
                    q.append((i,j))
                    ans[i][j] = 0
        level = 1
        while q:
            for _ in range(len(q)):
                i , j = q.popleft()
                for dx , dy in directions_straight:
                    x , y = i+dx , j + dy
                    if is_inbound(x,y) and ans[x][y]==-1:
                        ans[x][y]=level
                        q.append((x,y))
            level +=1
        return ans
            