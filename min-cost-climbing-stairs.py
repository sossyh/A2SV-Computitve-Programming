class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = {}

        def helper(i):
            if i == 0:
                return cost[i]
            
            if i == 1:
                return cost[i]
            
            if i not in dp:
                a = helper(i-1) 
                b = helper(i-2)
                dp[i] = min(a, b) +  cost[i]
                
            return dp[i]
        
        n = len(cost)
        ans = helper(n-1)
        
        return ans