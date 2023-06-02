class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        ans = -inf

        for i in arr:
            dp[i] = 1 + dp[i - difference]
            ans = max(ans, dp[i])
        
        return ans