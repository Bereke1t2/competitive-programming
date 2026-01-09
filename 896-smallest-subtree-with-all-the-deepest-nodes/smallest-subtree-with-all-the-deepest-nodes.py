# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,d):
            if not node:
                return d , node
            l_d  , left = dfs(node.left , d+1)
            r_d  , right = dfs(node.right , d+1)

            if l_d == r_d:
                return l_d , node
            elif l_d>r_d:
                return l_d , left
            return r_d , right
        _ , ans = dfs(root,0)
        return ans
            