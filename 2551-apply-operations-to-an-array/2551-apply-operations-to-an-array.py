class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i<len(nums)-1:
            if nums[i] and  nums[i] == nums[i+1]:
                res.append(2*nums[i])
                i +=1
            elif nums[i]:
                res.append(nums[i])
            i +=1
        if i==len(nums)-1:res.append(nums[i])
        while len(res)!=len(nums):res.append(0)
        return res

        