class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run = 0
        res = []
        for num in nums:
            run +=num
            res.append(run)
        return res