class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(num):
            if num==0:
                return 1
            if num<0:
                return 0
            if num not in  memo:
                for i in range(len(nums)):
                    memo[num] +=dp(num-nums[i])
            return memo[num]
        return dp(target)