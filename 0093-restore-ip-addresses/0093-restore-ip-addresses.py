class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        ans = []
        def dfs(i,stack):
            if i == N or len(stack)>4:
                if len(stack)==4:
                    ans.append('.'.join(stack.copy()))
                return
            for j in range(i+1,N+1):
                if (s[i:j] == '0' or not s[i:j].startswith('0')) and 0<=int(s[i:j]) <=255:
                    stack.append(s[i:j])
                    dfs(j,stack)
                    stack.pop()
        dfs(0,[])
        return ans
            
                    