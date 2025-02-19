# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr_node = head
        new_head = ListNode(0,head)
        prev = new_head
        while curr_node:
            while curr_node and curr_node.val == val:
                if curr_node.next:
                    curr_node.val = curr_node.next.val
                    curr_node.next = curr_node.next.next
                else:
                    prev.next = None
                    curr_node = None
            if curr_node:
                prev = curr_node
                curr_node = curr_node.next
        return new_head.next
        