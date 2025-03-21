class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(i,prev ,path):
            nonlocal n
            if i==n:
                ans.append(''.join(path))
                return
            path.append('1') 
            backtrack(i+1,1,path)
            path.pop()
            if prev==1:
                path.append('0') 
                backtrack(i+1,0,path)
                path.pop()
        backtrack(0,1,[])
        return ans
