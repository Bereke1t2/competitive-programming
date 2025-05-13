class Solution:
    def findComplement(self, num: int) -> int:
        temp = 0
        i = 0
        while num:
            if not num&1:
                temp = temp | 1<<i
            i+=1
            num >>=1
        return temp