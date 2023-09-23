class Solution:
    def dp(self, idx, nums, prev, memo):
        if idx in memo:
            return memo[idx]
        
        if idx >= len(nums):
            return 0
        
        longest = 0
        
        for i in range(idx, len(nums)):
            if nums[i] > prev:
                curr = self.dp(i+1, nums, nums[i], memo)
                longest = max(longest, curr + 1)
        
        memo[idx] = longest
        return longest
        
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        return self.dp(0, nums, -inf, memo)
        
        