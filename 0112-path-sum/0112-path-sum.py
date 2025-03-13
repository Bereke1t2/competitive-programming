# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root , Sum , targetSum):
        if not root.left and not root.right:
            return targetSum==Sum+root.val
        left = right = False
        if root.left:
            left = self.helper(root.left,Sum + root.val,targetSum)
        if root.right:
            right = self.helper(root.right,Sum + root.val,targetSum)

        return left or right 
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root,0,targetSum)
        
        
        