class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n))
        min_ = [inf]*n
        size = [1]*n
        def find(node):
            if parent[node]==node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1 , node2 , w):
            par1 , par2 = find(node1) , find(node2)

            if par1!=par2:
                if size[par1]<=size[par2]:
                    parent[par1] = parent[par2]
                    size[par2] +=size[par1]
                else:
                    parent[par2] = parent[par1]
                    size[par1] +=size[par2]
            min_[par2] = min(min_[par2] ,min_[par1], w)
            min_[par1] = min_[par2]
                
            return par1==par2
        
        for node1 , node2 , w in roads:
            union(node1-1 , node2-1 , w)
        return min_[find(0)]
        


