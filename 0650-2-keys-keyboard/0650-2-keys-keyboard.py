class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        visited = set()
        
        i = 2
        
        while i*i <= n:
            while n % i == 0:
                ans += i
                n //= i
            
            i += 1
        
        if n > 1:
            ans += n
        
        return ans
        
        
        