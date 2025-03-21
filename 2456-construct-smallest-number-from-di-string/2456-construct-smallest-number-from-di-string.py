class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        def backtrack(j,path,seen):
            if j==-1:
                ans.append(''.join([str(l) for l in path])[::-1])
                return 

            for i in range(9,0,-1):
                res = None
                if not path:
                    path.append(i)
                    seen.add(i)
                    res = backtrack(j-1 , path ,seen)
                    path.pop()
                    seen.discard(i)

                else:
                    num = path[-1] 
                    if not i in seen and ((pattern[j] == "I" and i<num) or (pattern[j] == "D" and i>num)):
                        path.append(i)
                        seen.add(i)
                        res = backtrack(j-1 , path ,seen)
                        path.pop()
                        seen.discard(i)
                if res:
                    return res
            return ''

        backtrack(len(pattern),[],set())
        ans.sort()
        return ans[0]
            


