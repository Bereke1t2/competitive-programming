class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        first = len(nums)
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>0:
                first = mid
                right = mid-1
            else:
                left = mid+1
        return max(len(nums)-first,first-nums.count(0))