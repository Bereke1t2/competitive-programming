class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path , seen):
            nonlocal res  , nums
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num not in seen:
                    path.append(num)
                    seen.add(num)
                    backtrack(path , seen)
                    path.pop()
                    seen.discard(num)
        backtrack([],set())
        return res