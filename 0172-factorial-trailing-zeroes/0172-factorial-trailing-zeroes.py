class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(5,n+1,5):
            num = i*(1<<16)
            for l in str(num)[::-1]:
                if l=='0':
                    count +=1
                else:
                    break
            
        return count 