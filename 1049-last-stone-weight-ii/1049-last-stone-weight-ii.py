class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones) 
        target = (total // 2) if total % 2 == 0 else (total // 2) + 1
        stones.sort()
        memo = {}
        
        def dp(idx, summ):
            
            if summ >= target or idx >= len(stones):
                return summ
            
            if (idx, summ) in memo:
                return memo[(idx, summ)]
            
            
            pick = dp(idx+1, summ + stones[idx])
            
            notpick = dp(idx+1, summ) 
            
            memo[(idx, summ)] = pick if abs(pick - target) <  abs(notpick - target) else notpick 
            return pick if abs(pick - target) <  abs(notpick - target) else notpick 
    
    
        a = dp(0, 0)
        print(a)
        
        return abs(a - (total - a))