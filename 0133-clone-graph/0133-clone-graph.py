"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        head = Node()
        co = defaultdict()
        if node==None:
            return None
        def dfs(node , head):
            if not node:
                return head
            if node in co:
                return co[node]
            head.val = node.val
            co[node] = head 
            for next_node in node.neighbors:
                head.neighbors.append(dfs(next_node,Node(1)))
            return head
        return dfs(node , head)