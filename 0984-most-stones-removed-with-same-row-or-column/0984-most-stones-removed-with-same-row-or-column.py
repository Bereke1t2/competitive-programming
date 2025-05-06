class DSU:
    def __init__(self):  
        self.parent = dict()
        self.row = dict()
        self.col = dict()
        self.size = defaultdict(lambda : 1)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        if x in self.row:
            r_x = self.row[x]
            par = self.find(r_x)
            self.parent[(x,y)] = par
            self.size[par] +=1
        else:
            self.find((x,y))
            self.row[x] = tuple([x,y])
        if y in self.col:
            if (x,y) in self.parent:
                r_x = self.find((x,y))
                r_y = self.find(self.col[y])
                if r_x != r_y:
                    if self.size[r_x]>self.size[r_y]:
                        self.size[r_x] +=self.size[r_y]
                        self.parent[r_y] = self.parent[r_x]
                    else:
                        self.size[r_y] +=self.size[r_x]
                        self.parent[r_x] = self.parent[r_y]
            else:
                r_x = self.col[y]
                par = self.find(r_x)
                self.parent[(x,y)] = par
                self.size[par] +=1
        else:
            self.find((x,y))
            self.col[y] = tuple([x,y])



class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()
        for x, y in stones:    
            dsu.union(x,y)
        for x, y in stones:
            dsu.find((x,y))
        _sum = 0
        for key, val in dsu.parent.items():
            if key == val:
                _sum += dsu.size[key] - 1
        return _sum