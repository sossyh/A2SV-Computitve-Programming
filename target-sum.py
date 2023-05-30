class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtracking(idx, summ):
            if idx >= len(nums):
                if target == summ:
                    return 1
                return 0
            
            state = (idx, summ)
            if state not in memo:
                ans1 = backtracking(idx+1, summ + nums[idx])
                ans2 = backtracking(idx+1, summ - nums[idx])
                memo[state] = ans1 + ans2

            return memo[state]

        backtracking(0, 0)
        
        return memo[(0,0)]