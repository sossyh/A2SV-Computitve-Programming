class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = max(nums)
        values = [0] * (n+1)
        
        for num in nums:
            values[num] += num
        
        memo = {}
        
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(values):
                return 0
            
            pick = values[idx] + dp(idx + 2)
            notpick = dp(idx+1)
            
            memo[idx] = max(pick, notpick)
            return max(pick, notpick)
        
        return dp(0)
                