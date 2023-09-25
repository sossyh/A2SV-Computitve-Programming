class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def dp(idx, buy = True):
            
            if (idx, buy) in memo:
                return memo[(idx, buy)]
            
            if idx >= len(prices):
                return 0
            
            maxprofit = 0
            
            if buy:
                take = -prices[idx] + dp(idx+1, not buy)
                nottake = dp(idx+1, buy)
                maxprofit = max(take, nottake)
            
            else:
                take = prices[idx] + dp(idx+2, not buy)
                nottake = dp(idx+1, buy)
                maxprofit = max(take, nottake)
            
            memo[(idx, buy)] = maxprofit
            
            return maxprofit
        
        return dp(0)