class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = set([0])
        q = deque([0])
        level = 0
        while q: 
            for _ in range(len(q)):
                room  = q.popleft()
                for curr_room in rooms[room]:
                    if curr_room not in seen:
                        seen.add(curr_room)
                        q.append(curr_room)
            if len(seen) == len(rooms):
                return True
        return False
