class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        prefix_mat = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                prefix_mat[row][col] = mat[row - 1][col - 1] + prefix_mat[row - 1][col] + prefix_mat[row][col - 1] - prefix_mat[row - 1][col - 1]
        
        ans = [[0] * cols for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                r1 = min(row + k + 1, rows)
                c1 = min(col + k + 1, cols)
                r2 = max(row - k, 0)
                c2 = max(col - k, 0)
                
                ans[row][col] = prefix_mat[r1][c1] - prefix_mat[r2][c1] - prefix_mat[r1][c2] + prefix_mat[r2][c2]
        
        return ans