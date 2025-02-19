# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 1
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        while stack:
            if stack.pop().val!=head.val:
                return False
            head = head.next
        return True

        