# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        q = deque()
        def dfs(node):
            if not node:
                return 
            if node.val%2==0:
                q.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        level = 1
        res = [0]
        while q:
            for _ in range(len(q)):
                node  = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
            if level == 3:
                while q:
                    res.append(q.popleft().val)
        return sum(res)
                