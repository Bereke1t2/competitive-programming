class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        count = 0
        nums.sort()
        for i in range(len(nums) - 1):
            minReq = lower - nums[i]
            maxReq = upper - nums[i]
            low = bisect_left(nums, minReq, i+1)
            high = bisect_right(nums, maxReq, i+1)
            count += high - low
        return count