class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [0] * n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        ans = []

        for i in range(self.pointer, self.n):
            if self.stream[i] == 0:
                break
            
            ans.append(self.stream[i])
        
        while self.pointer < self.n and self.stream[self.pointer]:
            self.pointer += 1
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)