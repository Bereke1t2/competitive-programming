# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        MIN , MAX = min(p.val , q.val) , max(p.val , q.val)
        if root.val >= MIN and root.val<= MAX:
            return root
        elif root.val >= MIN and root.val>= MAX:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)