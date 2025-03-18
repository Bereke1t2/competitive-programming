"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def pre(root):
            if not root:
                return 
            # print(root.val)
            res.append(root.val)
            for node in root.children:
                pre(node)
        pre(root)
        return res
        