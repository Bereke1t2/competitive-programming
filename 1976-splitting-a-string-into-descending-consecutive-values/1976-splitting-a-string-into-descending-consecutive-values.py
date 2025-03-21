class Solution:
    def splitString(self, s: str) -> bool:
        # nums = [int(num) for num in s]
        N = len(s)
        def backtrack(i,stack):
            if i==N:
                return len(stack)>1
            print(i,stack)
            for j in range(i+1,N+1):
                if not stack:
                    stack.append(int(s[i:j]))
                    if backtrack(j,stack):
                        return True
                    stack.pop()
                else:
                    if stack[-1] -1 == int(s[i:j]):
                        stack.append(int(s[i:j]))
                        if backtrack(j,stack):
                            return True
                        stack.pop()
            return False
                
        return backtrack(0,[])

            
            

