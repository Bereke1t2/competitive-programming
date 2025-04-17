class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        s = set([(r1,r2) for r1 ,r2 in roads])
        graph = [[0,_] for _ in range(n)]
        for e1 ,e2 in roads:
            graph[e1][0] +=1
            graph[e2][0] +=1
        graph.sort()
        max_ = 0
        for i in range(n):
            for j in range(i+1,n):
                if i!=j:
                    x , y = graph[i][1] , graph[j][1]
                    Sum = graph[i][0] + graph[j][0]
                    if (x,y) in s or (y , x) in s:
                        Sum -=1
                    max_ = max(max_ , Sum)
        return max_

        

        