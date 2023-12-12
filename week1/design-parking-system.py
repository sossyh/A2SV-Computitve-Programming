class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.bc = 0
        self.md = 0
        self.sm = 0
        
        

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.bc < self.big:
            self.bc += 1
            return True
        
        elif carType == 2 and self.md < self.medium:
            self.md += 1
            return True
        
        elif carType == 3 and self.sm < self.small:
            self.sm += 1
            return True
        
        return False
        

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)