class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        state = defaultdict(int)
        max_ = -1
        def dfs(node , dist , curr_dist):
            nonlocal state , max_
            if node ==-1 or state[node]==1:
                return
            if state[node]==-1:
                max_ = max(curr_dist - dist[node] , max_)
                return
            state[node] = -1
            dist[node] = curr_dist
            dfs(edges[node] , dist , curr_dist +1)
            state[node] = 1
        for node in range(len(edges)):
            dfs(node , defaultdict(int) , 0)
        return max_ if max_ else -1