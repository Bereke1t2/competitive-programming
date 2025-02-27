class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = [[0],[0]]
        for x1 , x2 in zip(grid[0],grid[1]):
            prefix[0].append(prefix[0][-1] + x1)
            prefix[1].append(prefix[1][-1] + x2)
        res = float('inf')
        for i in range(1,len(grid[0])+1):
            top = prefix[0][-1] - prefix[0][i]
            bottom = prefix[1][i-1]
            res = min(res,max(top,bottom))

        return res
