class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = {}
        
        
        def dp(idx, idxparityeven):
            if (idx, idxparityeven) in memo:
                return memo[(idx, idxparityeven)]
            
            if idx >= len(nums):
                return 0
            
            value = nums[idx] if idxparityeven else -1 * nums[idx]
            
            pick = dp(idx + 1, not idxparityeven) + value
            
            notpick = dp(idx + 1, idxparityeven)
            
            memo[(idx, idxparityeven)] = max(pick, notpick)
            return max(pick, notpick)
        
        return dp(0, True)
        
        