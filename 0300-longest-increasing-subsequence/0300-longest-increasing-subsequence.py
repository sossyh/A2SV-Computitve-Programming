class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dp(idx, lst):
            if idx in memo:
                return memo[idx]
            
            if idx >= len(nums):
                return 0
            
            max_length = 0
            for i in range(idx, len(nums)):
                if not lst or nums[i] > lst[-1]:
                    lst.append(nums[i])
                    a = dp(i + 1, lst)
                    max_length = max(max_length, a + 1)
                    lst.pop()
            
            memo[idx] = max_length
            return max_length
        
        return dp(0, [])
        