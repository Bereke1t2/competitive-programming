# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return max(nums[i] + nums[len(nums)-1-i] for i in range(len(nums)))

        