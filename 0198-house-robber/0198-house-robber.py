class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(idx):
            if idx == len(nums) -1:
                return nums[idx]
            
            if idx >= len(nums):
                return 0
            
            a = dp(idx+1)
            
            b = dp(idx+2)
            
            return max(a, b+nums[idx])
        
        return dp(0)