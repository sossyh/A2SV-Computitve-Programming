class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(total):
            if total >= target:
                return total == target

            # if total in memo:
                # return memo[total]
            if total not in memo:
                for i in nums:
                    memo[total] += dp(i+total)
                
            return memo[total]

        return dp(0)