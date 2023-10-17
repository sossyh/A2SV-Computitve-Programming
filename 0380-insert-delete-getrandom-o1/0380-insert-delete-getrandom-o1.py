class RandomizedSet:

    def __init__(self):
        self.hashset = {}
        self.mylist = []
        self.count = 0
        
    def insert(self, val: int) -> bool:
        if val not in self.hashset:
            self.hashset[val] = self.count
            self.count += 1
            self.mylist.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.hashset:
            validx = self.hashset[val]
            lastelet = self.mylist[-1]
            self.mylist[-1], self.mylist[validx] = self.mylist[validx], self.mylist[-1]
            self.mylist.pop()
            self.hashset[lastelet] = validx
            del self.hashset[val]
            self.count -= 1
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.mylist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()