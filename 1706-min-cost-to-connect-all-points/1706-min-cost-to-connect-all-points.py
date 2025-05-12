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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        uni = DSU(n)

        for i in range(n):
            for j in range(i+1 , n):
                x1 , y1 = points[i]
                x2 , y2  = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heappush(edges , (dist , i , j))


        count = 0
        while edges:
            dist , x, y = heappop(edges)
            count += (dist if not uni.union(x, y) else 0)
        return count