class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        row = [0]*rows
        col = [0]*cols

        for r in range(rows):
            for c in range(cols):
                row[r] = max(row[r],grid[r][c])
                col[c] = max(col[c],grid[r][c])
        count = 0

        for r in range(rows):
            for c in range(cols):
                count +=min(row[r],col[c]) - grid[r][c]
        return count
