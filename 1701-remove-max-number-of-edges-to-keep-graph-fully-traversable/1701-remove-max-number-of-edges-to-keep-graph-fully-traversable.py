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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n+1)
        bob= DSU(n+1)
        count = 0
        edges.sort(reverse=True)
        print(edges)
        for typ , node1 , node2 in edges:
            if typ==1:
                count +=alice.union(node1 , node2)
            elif typ==2:
                count += bob.union(node1 , node2)
            else:
                alice_s = alice.union(node1 , node2)
                bob_s = bob.union(node1 , node2)
                count +=( alice_s and bob_s)
        alice_par , bob_par = alice.find(1) , bob.find(1)
        for node in range(1 , n+1):
            if alice.find(node)!=alice_par or bob.find(node)!=bob_par:
                return -1
        return count