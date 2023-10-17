class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        memo = {}
        
        def dp(idx, summ):
            if (idx, summ) in memo:
                return memo[(idx, summ)]
            
            if idx >= len(nums):
                if summ == total // 2:
                    return True
                return False
            
            if dp(idx + 1, summ + nums[idx]):
                memo[(idx, summ)] = True
                return True
            
            if dp(idx + 1, summ):
                memo[(idx, summ)] = True
                return True
            
            memo[(idx, summ)] = False
            return False
        
        return dp(0, 0)
            
                