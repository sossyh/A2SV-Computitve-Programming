class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = -inf
        
        dp = [0] * len(values)
        dp[0] = values[0]
        
        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], (i + values[i]))
            ans = max(ans, (dp[i-1] + values[i] - i))
            
        return ans
                
        