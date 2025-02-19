class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [ 2*num -1 for num in nums]
        d = defaultdict(int)
        max_ = 0 
        Sum = 0
        d[0] = -1
        for index , num in enumerate(nums):
            Sum +=num
            if Sum in d:
                max_ = max(max_,index-d[Sum])
            else:
                d[Sum] = index
        return max_
