class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def good(cand):
            count = 0
            for num in quantities:
                count +=ceil(num/cand)
            return count<=n
        
        left , right = 1,max(quantities)
        ans = 1
        while left<=right:
            mid = (left + right)//2
            print(mid)
            if good(mid):
                right = mid -1
                ans =mid
            else:
                left  = mid + 1
        return ans