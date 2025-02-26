class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums) 
        ans_ind= 0
        min_ = float('inf')

        for i in range(1,n):
            nums[i] += nums[i-1]
        for i in range(n-1):
            curr_diff = int(abs(nums[i]//(i+1) - (nums[-1] - nums[i] )//(n-i-1)))
            if curr_diff< min_:
                ans_ind = i
                min_ = curr_diff
        curr_diff = int(abs(nums[-1]//(n) - 0))
        if curr_diff< min_:
            ans_ind = n-1
        return ans_ind

        