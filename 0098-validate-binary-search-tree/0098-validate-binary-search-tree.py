# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self , root):
        if not root:
            return (float('-inf') , float('inf') , True)
        
        left_max , left_min , left_state  = self.check(root.left)
        right_max , right_min , right_state  = self.check(root.right)

        if right_min<= root.val or left_max>= root.val or not (left_state and right_state):
            return (float('-inf') , float('inf') , False)
        return (max(left_max, right_max , root.val) , min(left_min , right_min , root.val) , True)



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _ , _ , ans = self.check(root)
        return ans