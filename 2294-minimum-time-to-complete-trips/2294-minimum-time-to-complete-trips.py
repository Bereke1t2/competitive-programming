class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def good(cand):
            count = 0
            for num in time:
                count += cand//num
            return count>=totalTrips
        left , right = 1,max(time)*totalTrips
        ans = 1
        while left<=right:
            mid = (left + right)//2
            if good(mid):
                right = mid -1
                ans =mid
            else:
                left  = mid + 1
        return ans