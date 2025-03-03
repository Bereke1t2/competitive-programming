class Solution:
    def canJump(self, nums: List[int]) -> bool:
        greedy = 0
        for index , num in enumerate(nums):
            greedy = max(greedy -1 , num)
            if greedy<1 and index +1 !=len(nums):
                return False
        return True

        