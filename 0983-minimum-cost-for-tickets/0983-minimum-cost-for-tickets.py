class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        
        def dp(idx, jump):
            if idx >= len(days):
                return 0
            
            if (idx, jump) in memo:
                return memo[(idx, jump)]
            
            curr_day = days[idx]
            total = inf
            
            if days[idx] > jump:
                
                one = dp(idx + 1, days[idx]) + costs[0]
                total = min(total, one)

                two = dp(idx + 1, days[idx] + 7 - 1) + costs[1]
                total = min(total, two)

                three = dp(idx + 1, days[idx] + 30 - 1) + costs[2]
                total = min(total, three)
                
            else:
                
                total = dp(idx+1, jump)
            
            memo[(idx, jump)] = total
            return total 
        
        return dp(0, 0)