class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')-1
        res = []
        for i in range(len(s)-1):
            if ones:
                res.append('1')
                ones -=1
            else:
                res.append('0')
        res.append('1')
        return ''.join(res)

        