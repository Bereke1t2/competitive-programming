# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self ,root1,root2):
        if not root1 and not root2:
            return None
        if not root1:
             root2.right = self.merge(root1,root2.right)
             root2.left = self.merge(root1,root2.left)
             return root2
        elif not root2:
             root1.right = self.merge(root1.right, root2)
             root1.left = self.merge(root1.left , root2)
             
        else:
            root1.val +=root2.val
            root1.right = self.merge(root1.right, root2.right)
            root1.left = self.merge(root1.left , root2.left)
        return root1
            

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        head = TreeNode(0,root1)
        head.left  = self.merge(root1 , root2)
        return head.left