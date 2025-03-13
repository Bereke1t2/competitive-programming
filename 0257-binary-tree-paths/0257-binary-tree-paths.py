# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return []
        def paths(root,path):
            path.append(str(root.val))
            if not root.left and not root.right:
                res.append('->'.join(path))
                path.pop()
                return
            if root.left:
                paths(root.left , path)
            if root.right:
                paths(root.right, path)
            path.pop()
        paths(root,[])
        return res

            
                

        