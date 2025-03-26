class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for num in grid:
            nums.extend(num)
        nums.sort()
        target = nums[len(nums)//2]
        count = 0
        for num in nums:
            if abs(num - target)%x:
                return -1
            count +=abs(num-target)//x
        return count