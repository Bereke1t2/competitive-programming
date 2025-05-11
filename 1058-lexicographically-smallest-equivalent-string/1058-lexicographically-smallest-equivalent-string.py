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
            if root_x > root_y:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
        return root_x == root_y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        nums1 = [ord(l) - ord('a') for l in s1]
        nums2 = [ord(l) - ord('a') for l in s2]
        p = [ord(l) - ord('a') for l in baseStr]
        ans = []

        uni = DSU(26)

        for i in range(len(nums1)):
            uni.union(nums1[i] , nums2[i])
        
        for num in p:
            ans.append(uni.find(num))
        
        ans = [chr(num+ord('a')) for num in ans]
        return ''.join(ans)

        
