class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        num = 0
        count = [0]*32
        max_ = inf
        left = 0
        for right in range(len(nums)):
            for i in range(32):
                if nums[right]>>i&1:
                    count[i] +=1
                    num |=1<<i
            while left<=right and num>=k:
                max_ = min(max_ , right - left+1)
                for i in range(32):
                    if nums[left]>>i&1:
                        count[i] -=1
                        if not count[i]:
                            num &=~(1<<i)
                left +=1
        return max_ if max_!=inf else -1
                