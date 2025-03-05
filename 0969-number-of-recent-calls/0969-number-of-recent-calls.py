class RecentCounter:

    def __init__(self):
        self.stack = []
        

    def ping(self, t: int) -> int:
        count = 1
        if self.stack:
            for i in range(len(self.stack)-1 , -1 ,-1):
                if t - self.stack[i]<=3000:
                    count +=1
                else:
                    break
        self.stack.append(t)
        return count


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)