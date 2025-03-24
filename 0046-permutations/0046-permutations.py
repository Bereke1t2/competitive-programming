class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        ans = []
        for index,num in enumerate(nums):
            remaining = nums[:index]+nums[index+1:]
            for permu in self.permute(remaining):
                ans.append([num]+permu)
        return ans