class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(num < 0 for row in grid for num in row)
