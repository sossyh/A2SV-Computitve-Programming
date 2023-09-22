class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        @cache
        def dp(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            a = dp(i+1)
            b = dp(i+2)
            
            return a+b
        

        return dp(0)