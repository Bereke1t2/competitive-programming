class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right = 0
        for left in range(len(nums)):
            if nums[left]==0:
                if left>right:
                    right = left+1
                while right<len(nums):
                    if nums[right]!=0:
                        nums[left] , nums[right] = nums[right] , nums[left]
                        break
                    right +=1
        

        