class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = set()
        Sum = len(grid)**2
        Sum = Sum*(Sum +1)//2
        total = sum(sum(g) for g in grid)
        for g in grid:
            for k in g:
                if k in s:
                    return [k,Sum + k - total]
                s.add(k)
            
