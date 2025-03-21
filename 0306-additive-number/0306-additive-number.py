class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def dfs(i,stack):
            if i == N:
                print(stack)
                return len(stack)>2
            for j in range(i+1,N+1):
                if len(stack)<2:
                    if num[i:j]=='0' or not num[i:j].startswith('0') :
                        stack.append(int(num[i:j]))
                        if dfs(j , stack):
                            return True
                        stack.pop()
                else:
                    if stack[-1] + stack[-2] == int(num[i:j]) and (num[i:j]=='0' or not num[i:j].startswith('0')):
                        stack.append(int(num[i:j]))
                        if dfs(j , stack):
                            return True
                        stack.pop()
            return False
        return dfs(0,[])

