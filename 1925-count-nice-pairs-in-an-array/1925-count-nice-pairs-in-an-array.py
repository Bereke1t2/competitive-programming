class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        count = 0
        for num in nums:
            count +=d[num - int(str(num)[::-1])]
            d[num - int(str(num)[::-1])] +=1
        return count % (10**9 + 7)


