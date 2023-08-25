class Solution:
    def totalMoney(self, n: int) -> int:
        a = n // 7
        total = 0
        start = 28
        
        for i in range(a):
            total += start
            start += 7
        
        start = a + 1
        for i in range(n-(a*7)):
            total += start
            start += 1           
        
        
        return total