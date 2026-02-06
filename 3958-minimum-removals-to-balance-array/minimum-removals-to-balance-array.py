class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = n

        for i in range(n):
            right = bisect_right(nums, nums[i] * k)
            window = right - i
            ans = min(ans, n - window)

        return ans
