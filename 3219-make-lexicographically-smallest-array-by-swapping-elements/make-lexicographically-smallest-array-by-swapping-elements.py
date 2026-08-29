class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        group = []
        Map = {}
        for num in sorted(nums):
            if not group or abs(num-group[-1][-1])>limit:
                group.append(deque())
            group[-1].append(num)
            Map[num] = len(group)-1
        res = []
        for num in nums:
            res.append(group[Map[num]].popleft())
        return res