from typing import List

class Solution:
    def __init__(self):
        self.dp = {}
    
    def poss1(self, v: List[int], i: int, t: int) -> bool:
        if t == 0:
            return True
        if t < 0 or i >= len(v):
            return False
        if (i, t) in self.dp:
            return self.dp[(i, t)]
        
        self.dp[(i, t)] = self.poss1(v, i + 1, t) or self.poss1(v, i + 1, t - v[i])
        return self.dp[(i, t)]
    
    def poss(self, v: List[int], q: List[List[int]], k: int) -> bool:
        n = len(v)
        
        for i in range(n):
            t = []
            for j in range(k):
                if q[j][0] <= i <= q[j][1]:
                    t.append(q[j][2])
            
            self.dp.clear()
            if not self.poss1(t, 0, v[i]):
                return False
        return True
    
    def minZeroArray(self, v: List[int], q: List[List[int]]) -> int:
        n, m = len(v), len(q)
        l, r = 0, m
        ans = m + 10
        
        while l <= r:
            mid = (r - l) // 2 + l
            if self.poss(v, q, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans if ans <= m else -1