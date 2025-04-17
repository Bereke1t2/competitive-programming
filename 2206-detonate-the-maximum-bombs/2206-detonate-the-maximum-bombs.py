class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        
        def check(i, j):
            x1, y1, r1 = bombs[i]
            x2, y2, _ = bombs[j]
            dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            return dist <= r1
        
        for i in range(n):
            for j in range(n):
                if i != j and check(i, j):
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for next_node in graph[node]:
                if next_node not in visited:
                    count += dfs(next_node, visited)
            return count
        
        max_detonations = 0
        for i in range(n):
            visited = set()
            max_detonations = max(max_detonations, dfs(i, visited))
        
        return max_detonations
