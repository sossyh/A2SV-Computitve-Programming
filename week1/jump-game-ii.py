class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0

        memo = {}

        def dp(idx):
            if idx in memo:
                return memo[idx]

            if idx == len(nums) - 1:
                return 0
            
            if idx > len(nums) - 1:
                return inf

            min_jump = inf

            
            for j in range(1, nums[idx] + 1):
                a = dp(idx + j) + 1
                min_jump = min(a, min_jump)
            
            memo[idx] = min_jump
            return min_jump
        
        return dp(0)