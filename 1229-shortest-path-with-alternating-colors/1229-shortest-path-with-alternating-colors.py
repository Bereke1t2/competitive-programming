class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1]*n

        graph = defaultdict(list)

        for e1 ,e2 in redEdges:
            graph[e1].append((e2,'r'))
        for e1 ,e2 in blueEdges:
            graph[e1].append((e2,'b'))

        q = deque([(0,0,'o')])
        seen = set([(0,'o')])

        while q:
            node , dist ,color = q.popleft()
            res[node] = min(dist , res[node] if res[node]!=-1 else float('inf'))

            for curr_node , curr_color in graph[node]:
                if (curr_node , curr_color) not in seen and color != curr_color:
                    q.append((curr_node , dist+1,curr_color))
                    seen.add((curr_node,curr_color))
        return res
