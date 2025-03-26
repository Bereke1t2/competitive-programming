# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        curr=head
        prev=None
        next=head
        c=k
        while (curr and c>0):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            c-=1
        if curr==None and c>0:
            curr=prev
            prev=None
            next=None
            while curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
        if c>0:
            return prev
        head.next=self.reverseKGroup(curr,k)
        return prev