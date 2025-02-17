class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        d = defaultdict(int)
        d[0] = 1
        Sum = 0
        for num in nums:
            Sum +=num
            if Sum % k in d:
                count += d[Sum%k]
            d[Sum%k] +=1
        return count
        