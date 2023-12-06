class Solution:
    def totalMoney(self, n: int) -> int:
        m = -1
        total = 0
        curr = 0


        for i in range(n):
            if i % 7 == 0:
                m += 1
                curr = m + 1
            
            else:
                curr += 1
            
            total += curr
        
        return total