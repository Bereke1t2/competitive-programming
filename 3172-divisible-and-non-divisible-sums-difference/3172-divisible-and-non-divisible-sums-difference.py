class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        sum_multiples = m * (k * (k + 1)) 
        return (n * (n + 1)) // 2 - sum_multiples