class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dp(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == len(nums) - 1:
                return 0
            
            if idx >= len(nums):
                return inf
            
            min_jump = inf
            
            for i in range(1, nums[idx] + 1):
                prev_jump = dp(idx + i)
                min_jump = min(min_jump, prev_jump + 1 )
            
            
            memo[idx] = min_jump
            return min_jump
        
        return dp(0)