# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        Sum = 0 

        def dfs(root,path):
            nonlocal Sum    
            if not root.left and not root.right:
                path.append(str(root.val))
                Sum += int(''.join(path))
                path.pop()
                return
            path.append(str(root.val))
            if root.left:
                dfs(root.left,path)
            if root.right:
                dfs(root.right,path)
            path.pop()
        dfs(root,[])
        return Sum