class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        c = Counter(nums)

        for num , count in c.items():
            if len(heap)==k:
                heappushpop(heap, (count , num))
            else:
                heappush(heap , (count , num))
        return [num for count , num in heap]