class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows , cols = len(maze) , len(maze[0])
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        
        def is_exit(i,j):
            return i==0 or j ==0 or j==cols-1 or i==rows-1
        
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = 0
        dist = 0
        while q:
            i , j = q.popleft()
            if is_exit(i,j) and [i,j]!=entrance:
                return maze[i][j]

            maze[i][j]=='x'
            for dx , dy in directions_straight:
                x , y = i + dx , j + dy
                if is_inbound(x , y) and maze[x][y]=='.':
                    maze[x][y] = (maze[i][j]+1)
                    q.append((x,y))
        return -1



        