class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr_sum +=nums[i+1]
            else:
                curr_sum = nums[i+1]
            max_sum = max(max_sum,curr_sum)
        return max_sum
