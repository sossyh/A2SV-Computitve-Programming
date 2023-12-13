class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        memo = {}

        def dp(idx, count_a, count_b):
            if idx >= len(costs):
                return 0

            if (idx, count_a, count_b) in memo:
                return memo[(idx, count_a, count_b)]

            
            moving_to_a = inf

            if count_a < len(costs) // 2:
                moving_to_a = dp(idx + 1, count_a + 1, count_b) + costs[idx][0]
            
            moving_to_b = inf

            if count_b < len(costs) // 2:
                moving_to_b = dp(idx + 1, count_a, count_b + 1) + costs[idx][1]

            memo[(idx, count_a, count_b)] = min(moving_to_a, moving_to_b) 
            return min(moving_to_a, moving_to_b)
        
        return dp(0, 0, 0)

            