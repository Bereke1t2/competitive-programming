class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        left , right = 0 , len(nums)-1
        while left<right:
            res.append(nums[left])
            res.append(nums[right])
            left +=1
            right -=1
        if left == right:
            res.append(nums[right])
        return res
        