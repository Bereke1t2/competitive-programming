# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def revevrse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev= curr
                curr = next_node 
            return prev
        if l1.next:
            l1 = revevrse(l1)
        if l2.next:
            l2 = revevrse(l2)
        carry = 0
        head = ListNode()
        temp = head
        while l1 or l2:
            sum1 = sum2 = 0
            if l1:
                sum1 = l1.val
                l1 = l1.next
            if l2:
                sum2 = l2.val
                l2 = l2.next
            total_sum = sum1 + sum2 + carry
            temp.next = ListNode(total_sum%10)
            carry =total_sum//10
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return revevrse(head.next)


