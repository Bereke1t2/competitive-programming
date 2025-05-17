class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if x<0:
            res = -res
        if res>(2**31)-1 or res<-2**31:
            res = 0
        return res
        
        