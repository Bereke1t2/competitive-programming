class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        count = 0
        res = ''
        def backtrack(path):
            nonlocal count , n , k , res
            if count==k:
                return
            if len(path)==n:
                count +=1
                if count==k:
                    res = ''.join(path)
                return
            for l in 'abc':
                if not path or path[-1]!=l:
                    path.append(l)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return res
            