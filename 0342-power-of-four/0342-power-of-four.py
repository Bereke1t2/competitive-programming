class Solution:
    def check(self, n):
        if n==1:
            return True
        if n%4 or n==0:
            return False
        return self.check(n//4)

    def isPowerOfFour(self, n: int) -> bool:
        return self.check(n)
        