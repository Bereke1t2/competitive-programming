# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        if len(graph)==0:
            return [] if k else [root.val]
        q  = deque([target.val])
        level =0
        res = [] 
        n = len(graph)
        seen = [False]*n
        seen[target.val] = True
        while q:
            if level == k:
                while q:
                    node = q.popleft()
                    res.append(node)
                return res
            for _ in range(len(q)):
                node = q.popleft()
                for next_node in graph[node]:
                    if not seen[next_node]:
                        seen[next_node] = True
                        q.append(next_node)
            level +=1
        return res
