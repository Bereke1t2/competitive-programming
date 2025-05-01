class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            if len(heap)==2:
                heappushpop(heap , num)
            else:
                heappush(heap , num)
        return (heap[0] -1)* (heap[1] -1)

        