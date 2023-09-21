class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(idx, buy = True):
            
            if idx == len(prices) - 1:
                return prices[idx] if not buy else 0
            
            if idx >= len(prices):
                return 0
            
            profit = 0
            
            if buy:
                take = -prices[idx] + dp(idx+1, not buy)
                nottake = 0 + dp(idx+1, buy)
                profit = max(take, nottake)
            else:
                take = prices[idx] + dp(idx+1, not buy)
                nottake = 0 + dp(idx+1, buy)
                profit = max(take, nottake)
            
            return profit
        
        return dp(0)