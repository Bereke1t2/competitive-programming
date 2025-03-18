class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(i,path):
            nonlocal n , nums , res
            if i==n:
                res.append(path)
                return 
            backtrack(i+1,path.copy())
            path.append(nums[i])
            backtrack(i+1,path.copy())
        backtrack(0,[])
        return res
        