class DetectSquares:

    def __init__(self):
        self.hash = defaultdict(int)
        self.lst = []
        

    def add(self, point: List[int]) -> None:
        self.hash[tuple(point)] += 1
        self.lst.append(point)
        

    def count(self, point: List[int]) -> int:

        total = 0
        x, y = point[0], point[1]
        
        for qx, qy in self.lst:
            if x == qx or y == qy or abs(qx - x) != abs(qy - y):
                continue
                
            first_point = (x, qy)
            second_point = (qx, y)
            total += self.hash[(x, qy)] * self.hash[(qx, y)]
        
        return total
                


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)