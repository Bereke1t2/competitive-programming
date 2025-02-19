class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        check = [0]*len(nums)
        for start , end in requests:
            check[start] +=1
            if end + 1 < len(nums):
                check[end +1] -=1
        for i in range(1,len(nums)):
            check[i] +=check[i-1]
        check.sort(reverse=True)
        Sum = 0
        for num , multip in zip(nums,check):
            Sum += (num * multip)
        return Sum  % (10**9 + 7   )