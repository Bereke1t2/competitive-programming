class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0
        nums.sort()
        left , right = 0 , len(nums) - 4
        min_ = float('inf')
        while right < len(nums):
            min_ = min(min_ , nums[right] - nums[left])
            left +=1
            right +=1
        return min_

        