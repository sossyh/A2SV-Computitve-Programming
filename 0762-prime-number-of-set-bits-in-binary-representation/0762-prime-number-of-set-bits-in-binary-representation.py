class Solution:
    def numset(self, n):
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        
        return count
            
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        for i in range(left, right+1):
            a = self.numset(i) 
            if a in primes:
                ans += 1
        
        return ans