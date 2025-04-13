from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns
        dis = [[-1] * m for _ in range(n)]  # Distance matrix
        q = deque()  # Queue for BFS
        
        # Initialize the distance matrix and queue
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dis[i][j] = 0  # Distance for '0' cells is 0

        # Arrays for movement in 4 directions
        delRow = [1, -1, 0, 0]
        delCol = [0, 0, 1, -1]

        # BFS traversal
        while q:
            row, col = q.popleft()

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                # Check bounds and if unvisited
                if 0 <= nrow < n and 0 <= ncol < m and dis[nrow][ncol] == -1:
                    dis[nrow][ncol] = dis[row][col] + 1  # Update distance
                    q.append((nrow, ncol))  # Add to the queue

        return dis  # Return the distance matrix