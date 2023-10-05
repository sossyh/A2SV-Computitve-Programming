class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dp = [inf for i in range(n)]
        dp[src] = 0
        prev = dp.copy()
        
        for i in range(k + 1):
            for u, v, w in flights:
                dp[v] = min(dp[v], prev[u] + w)
            prev = dp.copy()
        
        return dp[dst] if dp[dst] != inf else -1