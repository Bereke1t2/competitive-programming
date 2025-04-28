class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0

        left = 0
        score = Sum = 0
        for right in range(len(nums)):
            Sum +=nums[right]
            score = Sum*(right - left+1)
            while score>=k:
                Sum -=nums[left]
                left +=1 
                score = Sum*(right - left+1)
            count +=(right - left +1)
        return count 
