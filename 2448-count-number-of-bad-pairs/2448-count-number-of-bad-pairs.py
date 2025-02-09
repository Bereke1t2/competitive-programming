class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = 0
        N = len(nums)
        d = defaultdict(int)
        for i in range(N):
            count +=d[nums[i]-i]
            d[nums[i]-i] +=1
        return N*(N-1)//2 - count


        