class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        nums.sort()
        N = len(nums)
        min_ = float('inf')
        prefix = 0
        for i in range(N):
            min_ = min(min_ ,total_sum - 2*prefix + (2*i - N)*nums[i])
            prefix +=nums[i]
        return min_
