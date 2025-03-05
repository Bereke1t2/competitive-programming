class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            j = 0
            for right in range(len(q)):
                if j==len(pattern):break
                if pattern[j] == q[right]:j+=1
                elif ord(q[right])<ord('a'):break
            for right in range(right+1,len(q)):
                if ord(q[right])<ord('a'):
                    res.append(False)
                    break
            else:
                res.append(j==len(pattern))
        return res
            
