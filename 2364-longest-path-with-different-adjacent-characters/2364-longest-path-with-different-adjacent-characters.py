class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for cha , par in enumerate(parent):
            graph[par].append(cha)
        max_ = 0
        def dfs(node):
            nonlocal s , graph  , max_
            min_heap = []
            for next_node in graph[node]:
                if s[node]==s[next_node]:
                    dfs(next_node)
                    continue
                if len(min_heap)==2:
                    heappushpop(min_heap , dfs(next_node))
                else:
                    heappush(min_heap , dfs(next_node))
            l = len(min_heap)
            if l ==2:
                max_ = max(max_ , sum(min_heap) +1)
            min_heap.append(0)
            max_ = max(max_ , max(min_heap)+1)
            return max(min_heap)+1
        dfs(graph[-1][0])
        return max_
            
