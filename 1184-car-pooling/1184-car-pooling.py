class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0]*1001
        for passeng , start , end in trips:
            prefix[start] +=passeng
            prefix[end] -=passeng
        for i in range(1,1001):
            prefix[i] +=prefix[i-1]
        return max(prefix) <= capacity