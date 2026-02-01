class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sor = sorted(nums)
        if nums[0] == sor[0] or nums[0]==sor[1] or nums[0]==sor[2]:
            return sum(sor[:3])
        return sum(sor[:2]) + nums[0]