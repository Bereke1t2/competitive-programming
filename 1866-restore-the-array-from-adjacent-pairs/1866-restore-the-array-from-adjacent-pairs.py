class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for p1 , p2 in adjacentPairs:
            graph[p1].append(p2)
            graph[p2].append(p1)
        start , end = [num for num , val in graph.items() if len(val)==1]
        res = [start]
        seen = set(res)
        def dfs(node):
            nonlocal res , seen
            if node not in seen:
                res.append(node)
                seen.add(node)
                dfs(graph[node][0])
                if len(graph[node])>1:
                    dfs(graph[node][1])
        dfs(graph[start][0])
        return res
