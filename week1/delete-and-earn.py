class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * ((2 * pow(10, 4)) + 1)

        for num in nums:
            freq[num] += 1
        
        memo = {}
        
        def dp(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(freq):
                return 0
            
            pick = dp(idx + 2) + freq[idx] * idx

            not_pick = dp(idx + 1) 

            memo[idx] = max(pick, not_pick)
            return max(pick, not_pick)
        
        return dp(0)