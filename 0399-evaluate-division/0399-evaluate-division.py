class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:   
        graph = defaultdict(list)

        for i , e in enumerate(equations):
            e1 , e2 = e[0]  , e[1]
            graph[e1].append((e2 , values[i]))
            graph[e2].append((e1 , 1/values[i]))
        
        def dfs(node1 ,  node2 , ans , seen):
            if node1 == node2:
                return ans
            if node1 in seen:
                return 
            seen.add(node1)
            for next_node  , w in graph[node1]:
                res = dfs(next_node , node2 , ans*w , seen)
                if res:
                    return res
            seen.remove(node1)
        res = []
        for e1 , e2 in queries:
            if e1 not in graph or e2 not in graph:
                res.append(-1.0)
            else:
                ans = dfs(e1 , e2 , 1 , set())
                res.append(ans if ans else -1)
       
        return res
