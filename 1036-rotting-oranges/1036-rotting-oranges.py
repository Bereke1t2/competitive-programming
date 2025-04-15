class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mat = []
        d = {0:-1 , 1:float('inf') , 2:0}
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(d[grid[i][j]])
            mat.append(temp.copy())


        rows , cols = len(grid) , len(grid[0])
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def bfs(i , j):
            seen = defaultdict(int)

            q = deque([(i, j , 0)])

            while q:
                x , y , time = q.popleft()
                # print(x,y,time)
                mat[x][y] = min(mat[x][y] , time)

                time +=1
                for dx , dy in directions_straight:
                    new_x  , new_y = x+dx  , y + dy
                    if is_inbound(new_x,new_y) and grid[new_x][new_y]==1 and not (new_x ,new_y) in seen:
                        q.append((new_x, new_y,time))
                        seen[(new_x ,new_y)] +=1

        found = False
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    bfs(i,j)
                    found  = True
                if grid[i][j]==1:
                    found = True
        if not found:
            return 0
        max_ = max([max(nums) for nums in mat])
        return max_ if max_!=float('inf') else -1