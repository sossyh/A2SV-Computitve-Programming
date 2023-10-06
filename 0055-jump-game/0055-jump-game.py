class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dp(idx):
            if idx == len(nums) - 1:
                return True
            
            if idx >= len(nums):
                return False
            
            for i in range(1, nums[idx] + 1):
                if dp(idx + i):
                    return True
                
        return dp(0)
                
            
            
            
            