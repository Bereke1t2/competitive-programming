class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_len = 0
        left = 0
        temp = 0
        for right in range(len(nums)):
            while bool(temp & nums[right]):
                temp ^=nums[left]
                left +=1
            temp |=nums[right]
            max_len = max(max_len , right - left +1)
        return  max_len      