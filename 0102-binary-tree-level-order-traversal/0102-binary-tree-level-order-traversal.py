# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        def dfs(root,l):
            if not root:
                return 
            d[l].append(root.val)
            dfs(root.left,l+1)
            dfs(root.right,l+1)
        dfs(root,0)
        return list(d.values())

            
        