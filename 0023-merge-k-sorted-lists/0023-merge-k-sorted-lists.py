# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        temp =head
        heap = []
        for l in lists:
            while l:
                heappush(heap , l.val)
                l = l.next
        while heap:
            num = heappop(heap)
            temp.next = ListNode(num)
            temp = temp.next
        return head.next