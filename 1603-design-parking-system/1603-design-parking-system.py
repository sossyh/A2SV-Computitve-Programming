class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigs = big
        self.mediums = medium
        self.smalls = small
        self.small = 0
        self.medium = 0
        self.big = 0
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big < self.bigs:
                self.big += 1
                return True
            else:
                return False
            
        if carType == 2:
            if self.medium < self.mediums:
                self.medium += 1
                return True
            else:
                return False

        if carType == 3:
            if self.small < self.smalls:
                self.small += 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)