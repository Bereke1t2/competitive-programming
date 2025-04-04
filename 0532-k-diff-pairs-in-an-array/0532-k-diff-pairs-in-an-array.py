class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        if not k:
            c = Counter(nums)
            return sum(val>1 for val in c.values())
        count = 0
        for num in sorted(list(set(nums))):
            count +=seen[num - k]
            seen[num] |=1
        return count
            