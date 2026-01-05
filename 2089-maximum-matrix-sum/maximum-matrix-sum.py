class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count = 0
        sum_ = 0
        min_ = inf
        for row in matrix:
            for num in row:
                sum_ += abs(num)
                count += num<0
                min_ = min(min_ , abs(num))
        return sum_ - (2*min_ if count%2 else 0)