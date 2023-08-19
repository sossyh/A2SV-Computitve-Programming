class Solution:
    def countPrimes(self, n: int) -> int:
        isprime = [True for i in range(n+1)]
        isprime[0]  = False
        if n > 0:
            isprime[1] = False
        
        i = 2
        while i * i  <= n:
            
            if isprime[i]:
                j = i**2
                while j <= n:
                    isprime[j] = False
                    j += i

            i += 1

        count = 0
        
        for i in range(n):
            if isprime[i]:
                count += 1
        
        return count