class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n*t+1):
            pro = 1
            for num in str(i):
                pro *= int(num)
            if pro%t==0:
                return i