class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k =k 
        self.heap = []
        for num in nums:
            if len(self.heap)==k:
                heappushpop(self.heap , num)
            else:
                heappush(self.heap,num)

    def add(self, num: int) -> int:
            if len(self.heap)==self.k:
                heappushpop(self.heap , num)
            else:
                heappush(self.heap,num)
            return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)