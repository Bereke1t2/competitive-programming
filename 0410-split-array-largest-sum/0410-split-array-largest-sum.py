class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(target):
            nonlocal nums , k
            total_sum = 0
            count = 1
            for num in nums:
                if total_sum + num > target:
                    count +=1
                    total_sum = num
                else:
                    total_sum +=num
            return count <= k
        left , right = max(nums) , sum(nums)

        while left <= right:
            mid = (left+right)//2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        