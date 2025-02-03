class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = 1
        max_inc = max_dec = 1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                inc =1
                dec =1
            elif nums[i]<nums[i+1]:
                inc +=1
                dec =1
            else:
                dec +=1
                inc =1
            max_inc = max(max_inc,inc)
            max_dec = max(max_dec,dec)
        return max(max_dec,max_inc)

