class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        num = ""
        for c in s:
            if c.isnumeric():
                num +=c
            elif c == '[':
                if temp !="":
                    stack.append(temp)
                    temp = ""
                stack.append(num)
                num =""
            elif c ==']':
                if not stack[-1].isnumeric():
                    s = stack.pop() + temp 
                    temp = s
                word = temp
                i = stack.pop()
                print(i)
                print(stack)
                word *= int(i)
                while len(stack) != 0 and not stack[-1].isnumeric() :
                    s = stack.pop() + word
                    word = s
                stack.append(word)
                temp = ""
            
            else:
                temp +=c
            print(stack)
        if len(stack)!=0:
            word = stack.pop()
        else:
            word = ""
        stack.append(word+temp)
        return str(stack)[2:-2]


        