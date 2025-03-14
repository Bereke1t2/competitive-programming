class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:'abc' , 3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

        N= len(digits)
        res = []
        def constract(i , path):
            if i==N:
                if path:
                    res.append(''.join(path))
                return
            for l in d[int(digits[i])]:
                path.append(l)
                constract(i+1,path)
                path.pop()
        constract(0,[])
        return res
        