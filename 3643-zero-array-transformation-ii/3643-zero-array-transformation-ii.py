class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left , right = 0 , len(queries)
        def check(k,nums):
            temp = [0]*len(nums)

            for i in range(k):
                s , e, inc = queries[i]
                temp[s] -=inc
                if e +1< len(nums):
                    temp[e+1] +=inc
            Sum = 0
            for i in range(len(temp)):
                Sum +=temp[i]
                nums[i] +=Sum
            return 0==sum(1 for num in nums if num>0)
        res = -1
        while left <= right:
            k = (left + right)//2
            if check(k,nums.copy()):
                right = k-1
                res = k
            else:
                left = k + 1
        return res
        

