class Node:
     def __init__(self,k):
        self.val = k
        self.next = None
class MyStack:

    def __init__(self):
        self.head = Node(0)

    def push(self, x: int) -> None:
        curr = Node(x)
        curr.next = self.head.next
        self.head.next = curr
        

    def pop(self) -> int:
        val = None
        if self.head.next:
            val = self.head.next.val
            self.head.next = self.head.next.next
        return val
            

    def top(self) -> int:
        if self.head.next:
            return self.head.next.val
        

    def empty(self) -> bool:
        return self.head.next == None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()