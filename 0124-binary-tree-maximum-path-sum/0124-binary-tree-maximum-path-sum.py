# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = float('-inf')

        def dfs(node):
            nonlocal max_
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            max_ = max(max_ , left + right + node.val)

            return max(max(right, left)+ node.val , 0)
        dfs(root)
        return max_