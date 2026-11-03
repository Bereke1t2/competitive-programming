class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ = max(nums)
        ans = 0
        for num in nums:
            ans +=max_ - num
        return ans