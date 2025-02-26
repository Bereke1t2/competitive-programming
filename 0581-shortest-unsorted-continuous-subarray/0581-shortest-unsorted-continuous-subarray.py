class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start , end  = -1 , -2
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] !=sorted_nums[i]:
                end = i
                if start == -1:
                    start = i
        return end - start + 1
        