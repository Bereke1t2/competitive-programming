class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left , right = 0, int(c**0.5)
        while left <= right:
            Sum = left**2 + right**2
            if Sum==c:
                return True
            elif Sum>c:
                right -=1
            else:
                left +=1
        return False
        