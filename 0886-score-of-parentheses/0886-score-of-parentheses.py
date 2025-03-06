class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for t in s:
            if t=='(':
                stack.append(t)
            else:
                if str(stack[-1]).isdigit():
                    suum = 0
                    while str(stack[-1]).isdigit():
                        suum +=stack.pop()
                    stack.pop()
                    stack.append(suum*2)
                else:
                    stack.pop()
                    stack.append(1)
        return sum(stack)


        