class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.append(0)
        
        memo = {}
        
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(cost):
                return 0
            
            a = dp(idx + 1)
            b = dp(idx + 2)
            
            total = cost[idx] + min(a, b)
            
            memo[idx] = total
            return total
        
        return min(dp(0), dp(1))