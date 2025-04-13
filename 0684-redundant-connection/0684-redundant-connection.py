class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = [-1]*(N+1)
        
        def find(n):
            if parent[n]<0:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1,n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return True
            if parent[p1] < parent[p2]:
                parent[p1] +=parent[p2]
                parent[p2] = p1
            else:
                parent[p2] +=parent[p1]
                parent[p1] = p2

            return False
        for n1 , n2 in edges:
            if union(n1,n2):
                return [n1,n2]
        return [-1,-1]

        