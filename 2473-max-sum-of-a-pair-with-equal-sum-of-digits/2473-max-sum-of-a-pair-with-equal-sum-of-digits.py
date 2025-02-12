class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        d = {}
        for num in nums:
            sum_d = sum([int(num) for num in str(num)])
            if sum_d in d:
                res = max(res,d[sum_d]+num)
                d[sum_d] = max(num,d[sum_d])
            else:
                d[sum_d] = num
        return res

        