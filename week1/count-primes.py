class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        primes = [True for i in range(n)]

        primes[0] = False
        primes[1] = False

        for i in range(n):
            j = i * i
            if primes[i]:
                while j < n:
                    primes[j] = False
                    j += i
        
        count = 0

        for i in range(len(primes)):
            if primes[i]:
                count += 1
        
        return count

        
        