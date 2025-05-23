class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dp(i , sum ,temp):
            nonlocal res
            if sum==target:
                res.append(temp.copy())
                return
            if i>=len(candidates) or sum>target:
                return 
            temp.append(candidates[i])
            dp(i+1 , sum + candidates[i] , temp)
            temp.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dp(i+1 , sum , temp)
        dp(0 , 0 ,[])
        return res

        