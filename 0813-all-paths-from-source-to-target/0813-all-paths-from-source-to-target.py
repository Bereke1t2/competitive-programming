class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(node , path):
            if node == len(graph)-1:
                path.append(node)
                res.append(path.copy())
                path.pop()
                return
            path.append(node)
            for next_node in graph[node]:
                dfs(next_node,path)
            path.pop()
        dfs(0,[])
        return res

            
        