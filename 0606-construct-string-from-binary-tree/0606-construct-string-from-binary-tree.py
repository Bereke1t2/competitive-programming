# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ''
            res =  [str(node.val)]
            if node.right or node.left:
                res.append("(")
                left = dfs(node.left)
                res.extend(left)
                res.append(')')
                if node.right:
                    right = dfs(node.right)
                    res.append('(')
                    res.extend(right)
                    res.append(')')
            return res
        return ''.join(dfs(root))

