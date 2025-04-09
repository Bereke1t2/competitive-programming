class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for e1 ,e2 in edges:
            graph[e2].append(e1)
        ans = []
        for i in range(n):
            if not len(graph[i]):
                ans.append(i)
        if len(ans)==1:
            return ans[0]
        return -1