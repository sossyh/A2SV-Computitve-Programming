class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        
        is_prime = [True for i in range(n)]
        
        is_prime[0] = False
        
        if n > 1:
            is_prime[1] = False
        
        i = 2
        
        while i * i < n:
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
            
            i += 1
        
        count = 0
        
        for i in is_prime:
            if i:
                count += 1
        
        
        return count
        
        