# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        cary = 0
        while l1 or l2 or cary:
            total = cary
            if l1:
                total +=l1.val
                l1 = l1.next
            if l2:
                total +=l2.val
                l2 = l2.next
            cary = total//10
            temp.next = ListNode(total%10)
            temp = temp.next
        return head.next



        




        