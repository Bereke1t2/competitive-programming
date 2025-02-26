class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ = 0
        min_ = 0
        max_sum = 0
        min_sum =  0
        for num in nums:
            max_sum = max(max_sum + num , num)
            min_sum = min(min_sum +num , num)
            max_ = max(max_, max_sum)
            min_ = min(min_, min_sum)
        return max(max_ , - min_)

        