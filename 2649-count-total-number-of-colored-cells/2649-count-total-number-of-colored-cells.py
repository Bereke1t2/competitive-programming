class Solution:
    def coloredCells(self, n: int) -> int:
        def get(n):
            if n == -1:
                return 1
            return n*4 + 4 + get(n-1)
        return get(n-2)        