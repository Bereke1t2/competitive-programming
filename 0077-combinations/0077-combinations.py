class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        choose = [num for num in range(1,n+1)]
        res = []
        def backtrack(i,path):
            if len(path)==k:
                res.append(path)
                return
            if i==n:
                if len(path)==k:
                    res.append(path)
                return
            backtrack(i+1,path.copy())
            path.append(choose[i])
            backtrack(i+1,path.copy())
            path.pop()
        backtrack(0,[])
        return res