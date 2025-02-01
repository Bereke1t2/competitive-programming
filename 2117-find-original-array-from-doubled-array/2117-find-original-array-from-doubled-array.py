class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        q = deque()
        changed.sort()
        res = []
        for c in changed:
            if q and 2*q[0]==c:
                res.append(q.popleft())
                continue
            else:
                q.append(c)
        if q:
            return []
        else:
            return res
