class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = [nums[i] for i in range(len(nums)-1,-1,-1) if nums[i]>0]
        negetive = [nums[i] for i in range(len(nums)-1,-1,-1) if nums[i]<0]
    
        res = []
        for i in range(len(nums)):
            if postive:
                res.append(postive.pop())
            if negetive:
                res.append(negetive.pop())
        return res
        