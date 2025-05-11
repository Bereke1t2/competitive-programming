
class DSU:
    def __init__(self, size):  
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
        return root_x == root_y


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        min_e = []
        min_q = []
        uni = DSU(n+1)
        ans = [False] *len(queries)
        for index , q in enumerate(queries):
            heappush(min_q , q[::-1] +[index])
        
        for e in edgeList:
            heappush(min_e , e[::-1])

        while min_q:
            limit , node1 , node2 , index = heappop(min_q)
            while min_e and min_e[0][0]<limit:
                _ , node_1 , node_2 = heappop(min_e)
                uni.union(node_1 , node_2)
            ans[index] = uni.find(node1 )==uni.find(node2)
        return ans
            