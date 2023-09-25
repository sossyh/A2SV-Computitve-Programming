class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        evenc, oddc = 0, 0
        
        for i in range(32):
            if i % 2 == 0 and n & (1 << i):
                evenc += 1
            if i % 2 == 1 and n & (1 << i):
                oddc += 1
        
        
        return [evenc, oddc]