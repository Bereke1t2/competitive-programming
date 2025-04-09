class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_ = min(nums)
        if min_<k:
            return -1
        dist = len(set(nums))

        return dist - int(min_==k)