class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        graph = defaultdict(list)

        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col]:
                    graph[col].append(row)
                    graph[row].append(col)

        def dfs(node):
            if node in seen:
                return 
            
            seen.add(node)
            for next_node in graph[node]:
                dfs(next_node)
        
        count = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
                count +=1

        return count