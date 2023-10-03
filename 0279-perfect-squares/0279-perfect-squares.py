class Solution:
    def numSquares(self, n: int) -> int:
        
        memo = {}
        def dp(currsum):
            if currsum in memo:
                return memo[currsum]
            
            if currsum == 0:
                return 0
            
            if currsum < 0:
                return float('inf')
            
            mini = currsum
            i = 1
            
            while i * i <= currsum:
                a = dp(currsum - (i*i))
                mini = min(mini, a + 1)
                i += 1
            
            
            memo[currsum] = mini
            return mini
        
    
        return dp(n)