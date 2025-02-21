# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even = odd.next
        even_start = even 
        place = 3
        temp = even.next
        while temp:
            if place%2:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            temp = temp.next
            place +=1
        odd.next = even_start
        even.next = None
        return head

        