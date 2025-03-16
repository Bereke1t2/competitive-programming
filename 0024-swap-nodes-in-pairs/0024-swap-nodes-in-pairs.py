# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(root):
            if not root or not root.next:
                return root
            temp = root.next.next
            ans  = root.next
            root.next.next = root
            root.next = swap(temp)
            return ans
        return swap(head)