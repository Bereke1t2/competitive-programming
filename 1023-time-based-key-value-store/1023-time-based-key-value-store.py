class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        left , right = 0, len(self.store[key])-1
        while left <= right:
            mid = (left+right)//2
            if self.store[key][mid][1]==timestamp:
                return self.store[key][mid][0]
            if timestamp<=self.store[key][mid][1]:
                right = mid-1
            else:
                left = mid +1

        if right ==-1:
            return ""
        return self.store[key][right][0]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)