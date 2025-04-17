class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        iland = defaultdict(list)
        rows , cols = len(grid1) , len(grid1[0])
        directions_straight = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def is_inbound(x, y):
            return 0 <= x < rows and 0 <= y < cols
        def dfs(i,j ,iland_num):
            if not is_inbound(i,j) or not grid2[i][j]:
                return 
            grid2[i][j] = 0
            iland[iland_num].append((i,j))
            for dx ,dy in directions_straight:
                dfs(i+dx ,j+dy,iland_num)
        count = 1
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j]:
                    dfs(i,j,count)
                    count +=1
        count = 0
        for iland_num in iland:
            for i ,j in iland[iland_num]:
                if not grid1[i][j]:break
            else:
                count +=1
        return count
                