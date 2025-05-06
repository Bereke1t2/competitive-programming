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
    def removeStones(self, stones: List[List[int]]) -> int:
        id = defaultdict(int)
        num = 1
        for point in stones:
            id[tuple(point)] = num
            num +=1
        
        uni = DSU(num)
        for i in range(len(stones)):
            for j in range(i+1 ,len(stones) ):
                if stones[i][1]==stones[j][1] or stones[i][0]==stones[j][0]:
                    uni.union(id[tuple(stones[i])] , id[tuple(stones[j])])
        count = 0
        for i in range(1,num):
            if uni.parent[i]==i:
                count +=(uni.size[i]-1)
        return count


