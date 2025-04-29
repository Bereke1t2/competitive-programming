class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap= []
        for stone in stones:
            heappush(heap , - stone)
        
        while len(heap)>1:
            val1 = - heappop(heap)
            val2 = - heappop(heap)
            stone = val1 - val2
            if stone:
                heappush(heap , - stone)
        return 0 if len(heap)==0 else -heap[0]

