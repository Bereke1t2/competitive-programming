class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for bit_index in range(32):
            count = 0
            for index in range(len(nums)):
                count += (nums[index]>>bit_index & 1)
            if count%3==1: 
                ans = ans | 1<<bit_index
        if ans >= 1<<31: 
            ans -= 1<<32
        return ans
