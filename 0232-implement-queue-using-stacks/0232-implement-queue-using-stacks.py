class MyQueue:

    def __init__(self):
        self.stack = []
        self.back = 0
        self.front = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.front +=1

        

    def pop(self) -> int:
        self.back +=1
        return self.stack[self.back - 1]
        

    def peek(self) -> int:
        return self.stack[self.back]

    def empty(self) -> bool:
        return  self.front - self.back==0        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()