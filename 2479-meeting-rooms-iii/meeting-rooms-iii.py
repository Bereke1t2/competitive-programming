class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0]*n
        free = [i for i in range(n)]
        inuse = []

        for s , e in meetings:
            while inuse and inuse[0][0]<=s:
                _  , room = heappop(inuse)
                heappush(free, room)
            
            if not free:
                end_time , room = heappop(inuse)
                e = end_time + e- s
                heappush(free , room)
            room = heappop(free)
            count[room] +=1
            heappush(inuse , (e , room))
        
        return count.index(max(count))