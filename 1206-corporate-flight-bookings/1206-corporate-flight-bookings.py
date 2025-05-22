class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for left , right , add in bookings:
            ans[left] +=add
            if right<n:
                ans[right+1] -=add
        for i in range(1,len(ans)):
            ans[i] +=ans[i-1]
        return ans[1:]