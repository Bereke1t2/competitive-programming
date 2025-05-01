class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        def dist(x,y):
            return x**2 +y**2
        for x, y in points:
            if len(res)==k:
                heapq.heappushpop(res,(-dist(x,y),(x,y)))
            else:
                heapq.heappush(res,(-dist(x,y),(x,y)))
        return [point for _ , point in res] 
            
        