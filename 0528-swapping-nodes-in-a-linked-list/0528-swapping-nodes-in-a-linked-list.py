# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = last = fast = head
        count_f = count_s = 0
        while fast:
            if  count_f != k-1:
                first = first.next
                count_f +=1
            if count_s!=k:
                count_s +=1
            else:
                last = last.next
            fast = fast.next
        first.val  , last.val = last.val , first.val
        return head