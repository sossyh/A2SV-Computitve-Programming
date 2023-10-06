class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        memo = {}
        
        def dp(idx, count_a, count_b):
            
            if (idx, count_a, count_b) in memo:
                return memo[(idx, count_a, count_b)]
            
            if idx >= len(costs):
                return 0
            
            in_city_a = inf
            if count_a != n // 2:
                in_city_a = dp(idx + 1, count_a + 1, count_b) + costs[idx][0]
            
            in_city_b = inf
            if count_b != n // 2:
                in_city_b = dp(idx + 1, count_a, count_b + 1) + costs[idx][1]
            
            
            memo[(idx, count_a, count_b)] = min(in_city_a, in_city_b)
            return min(in_city_a, in_city_b)
        
        return dp(0, 0, 0)
                
                
            