class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i, curr_sum):
            if i >= len(coins) or curr_sum >= amount:
                return 0 if curr_sum == amount else inf
            
            state = (i, curr_sum)
            if state not in memo:
                memo[state] = min(1 + dp(i, curr_sum + coins[i]), dp(i+1, curr_sum))
            
            return memo[state]
        
        ans = dp(0, 0)
        return ans if ans != inf else -1