class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_num = float('-inf')
        left = right = 0
        Sum =0
        while right<len(nums):
            if right - left==k:
                max_num = max(max_num,Sum)
                Sum -=nums[left]
                left +=1
            Sum +=nums[right]
            right +=1
        return max(max_num,Sum)/k
                
