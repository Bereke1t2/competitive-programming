class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = curr_sum = float('-inf')
        for num in nums:
            curr_sum = max(num , curr_sum + num)
            total_sum = max(total_sum , curr_sum)
        return total_sum