class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '-+*/':
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t=='+':
                    resulte = a+b
                elif t=='-':
                    resulte = a-b
                elif t=='*':
                    resulte = a*b
                else:
                    resulte = int(a/b)
                stack.append(resulte)
        return stack[-1] 

        