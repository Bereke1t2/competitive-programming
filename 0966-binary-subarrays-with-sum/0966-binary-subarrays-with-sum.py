class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count  = 0
        seen = defaultdict(int)
        seen[0] = 1
        Sum = 0
        for index , num in enumerate(nums):
            Sum +=num
            if Sum-goal in seen:
                count +=seen[Sum - goal]
            seen[Sum] +=1
        return count



        