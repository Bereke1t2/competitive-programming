# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        q =  deque()
        q.append([root,0])
        if not root:
            return []
        temp = []
        while q:
            node , level = q.popleft()
            d[level].append(node.val)
            if node.left:
                q.append([node.left , level +1])
            if node.right:
                q.append([node.right , level +1])
        return list(d.values())

