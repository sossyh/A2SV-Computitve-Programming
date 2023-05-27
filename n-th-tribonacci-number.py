class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i <= 1:
                return i
            if i == 2:
                return 1
            
            if i not in memo:
                memo[i] =  helper(i-1) + helper(i-2) + helper(i-3)
            
            return memo[i]
        
        return helper(n)