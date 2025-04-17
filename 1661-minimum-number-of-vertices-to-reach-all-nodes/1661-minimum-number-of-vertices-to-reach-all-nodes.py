class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for e1 ,e2 in edges:
            graph[e2].append(e1)
        return [i for i in range(n) if not graph[i]]