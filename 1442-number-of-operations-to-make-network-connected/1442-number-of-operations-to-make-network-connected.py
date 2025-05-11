class DSU:
    def __init__(self, size):  
        self.parent = list(range(size))
        self.size = [1] * size
        self.connected = 1
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
            self.connected +=1
        return root_x == root_y


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uni = DSU(n)
        count = 0
        for node1 , node2 in connections:
            count += uni.union(node1 ,node2)
        total = len(connections)
        total -=count
        return n - total -1 if count + uni.connected>=n else -1
