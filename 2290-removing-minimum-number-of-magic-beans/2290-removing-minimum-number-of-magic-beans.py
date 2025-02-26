class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        N = len(beans)
        beans.sort()
        min_ = float('inf')
        Sum = sum(beans)
        for i in range(N):
            min_ = min(min_, Sum - ((N-i)*beans[i]))
        return min_
        