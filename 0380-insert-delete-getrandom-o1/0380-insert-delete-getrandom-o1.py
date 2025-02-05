class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.store2= []
        

    def insert(self, val: int) -> bool:
        if not val in self.store:
            self.store2.append(val)
            self.store[val] = len(self.store2)-1
            return  True
        return False

    def remove(self, val: int) -> bool:
        if val in self.store:
            num = self.store2[-1]
            index = self.store[val]
            self.store2[index] = num
            self.store2.pop()
            self.store[num] = index
            del self.store[val]
            return  True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.store2)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()