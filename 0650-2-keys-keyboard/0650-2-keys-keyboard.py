class Solution:
    def devisors(self, n):
        
        i = (n // 2) 
        
        while i > 1:
            if n % i == 0:
                return i
            
            i -= 1
        
        return "prime"
    
    def minSteps(self, n: int) -> int:
        
        dp = [i for i in range(n+1)]
        
        for i in range(n+1):
            if i == 1:
                dp[i] = 0
            elif i == 2:
                dp[i] = 2
            
            elif self.devisors(i) == "prime":
                dp[i] = i
            
            else:
                a = self.devisors(i)
                b = i // a
                dp[i] = dp[a] + b
        
        
        return dp[n]
        