class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]

        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1 , node2):
            parent1 , parent2 = find(node1) , find(node2)

            if s[parent1]<s[parent2]:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2
        
        for node1 , node2 in pairs:
            union(node1 , node2)
        
        d = defaultdict(list)
        l = defaultdict(list)
        for i in range(len(s)):
            par = find(i)
            d[par].append(i)
            l[par].append(s[i])

        ans = [0]*len(s)

        for key in d:
            indexs = sorted(d[key])
            letters = sorted(l[key])
            for index , lett in zip(indexs , letters):
                ans[index] = lett
        return ''.join(ans)



