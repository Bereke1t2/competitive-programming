class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        for i in range(len(nums)):
            if temp == nums[i:] + nums[:i]:
                return True
        return False     