class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        return len(c) - (0 in c)