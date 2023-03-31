class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        while n > 0:
            before = n & 1 
            i = (n >> 1)
            after = i & 1
            if before == after:
                return False
            n >>= 1
        
        return True
        