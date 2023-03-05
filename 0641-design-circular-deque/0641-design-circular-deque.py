class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.que = []
        

    def insertFront(self, value: int) -> bool:
        if len(self.que) == self.size:
            return False
        else:
            self.que.append(value)
            for i in range(len(self.que)-1):
                self.que.append(self.que.pop(0))
            return True
        
        

    def insertLast(self, value: int) -> bool:
        if len(self.que) == self.size:
            return False
        else:
            self.que.append(value)
            return True

        

    def deleteFront(self) -> bool:
        if len(self.que) != 0:
            self.que.pop(0)
            return True
        else:
            return False
        
        
    def deleteLast(self) -> bool:
        if len(self.que) != 0:
            self.que.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.que) != 0:
            return self.que[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.que) != 0:
            return self.que[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.que) == 0

    def isFull(self) -> bool:
        return len(self.que) == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()