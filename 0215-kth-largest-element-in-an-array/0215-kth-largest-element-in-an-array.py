class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,-num)
        val = 0
        while k:
            val = - heappop(heap)
            k -=1
        return val