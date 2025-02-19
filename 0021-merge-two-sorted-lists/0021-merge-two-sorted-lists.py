# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = ListNode(0,None)
        head = ListNode(0,curr_node)
        p1 , p2 = list1 , list2
        while p1 or  p2 :
            if (p1 and not p2) or  (p1 and p2  and p1.val<p2.val):
                curr_node.next = p1
                curr_node = curr_node.next
                p1 = p1.next
            if (p2 and not p1) or (p1 and p2  and p1.val>=p2.val):
                curr_node.next = p2
                curr_node = curr_node.next
                p2 = p2.next 
        return head.next.next


