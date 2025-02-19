class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        Sum = sum(nums)
        pre = 0
        for index , num in enumerate(nums):
            Sum -=num 
            if Sum == pre:
                return index
            pre +=num
        return -1
        