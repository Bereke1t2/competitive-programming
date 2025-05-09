class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        @cache
        def count(current , index):
            if current<0:
                return 0
            if current == 0:
                return 1


            p = pow(index , x , MOD)
            if p>current:
                return 0
            
            total = 0
            total +=count(current - p , index+1)
            total +=count(current , index + 1)

            return total%MOD
        return count(n , 1)
       