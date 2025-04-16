class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])
        height = [[-1] * C for _ in range(R)]
        q = deque()
        for i in range(R):
            for j in range(C):
                if isWater[i][j]==1:
                    height[i][j]=0
                    q.append((i,j))

        while q:
            row , col = q.popleft()
            h = height[row][col]

            dirc = [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]
            for r , c in dirc:
                if 0<=r<R and 0<=c<C and height[r][c]==-1:
                    height[r][c] = h+1
                    q.append((r,c))

        return height