class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = defaultdict(int)
        def Pow(x,n):
            if n==-1:
                return 1/x
            if n ==0:
                return 1
            if n in memo:
                return memo[n]
            if n%2:
                memo[n] = Pow(x,n-1)*x
            else:
                memo[n]= Pow(x,n//2)
                return memo[n]*memo[n]
            return memo[n]
        return Pow(x,n)