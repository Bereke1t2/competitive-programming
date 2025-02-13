class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = right = 0 
        max_len = 0
        while right<len(nums):
            while zeros > k:
                zeros -=1-nums[left]
                left +=1
            max_len = max(max_len,right - left)
            zeros +=1-nums[right]
            right +=1
        if zeros<=k:
            max_len = max(max_len,right - left)
        return max_len
            