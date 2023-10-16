class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        if n == 0:
            return 1
        
        
        
        if n % 2 == 1:
            a = self.myPow(x, abs(n) // 2)
            value = a * a * x
            if n < 0:
                return 1 / (value)
            return value
        else:
            a = self.myPow(x, abs(n) // 2)
            value = a * a
            if n < 0:
                return 1/(value)
            return value
        
        