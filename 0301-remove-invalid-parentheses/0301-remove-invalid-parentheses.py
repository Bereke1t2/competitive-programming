class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        open = 0
        n = len(s)
        for i in range(n):
            open +=s[i]=='('
            if s[i]==')':
                if open:
                    open -=1
                    count +=2
            if not s[i] in '()':
                count +=1
        res = set()
        def dfs(i,open , path):
            nonlocal s ,res, count
            if i==n or len(path)>count:
                if len(path) ==count and open==0:
                    res.add(''.join(path.copy()))
                return
            dfs(i+1,open ,path)
            if s[i]==")":
                if open:
                    path.append(s[i])
                    dfs(i+1,open -1  ,path)
                    path.pop()
                else:
                    return
            else:
                path.append(s[i])
                dfs(i+1,open + (s[i]=='(') , path)
                path.pop()
        dfs(0,0,[])
        return list(res) if res else ['']

            