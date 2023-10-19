class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dp(idx1, idx2):
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]
            
            if idx1 >= len(word1) or idx2 >= len(word2):
                return max(len(word1) - idx1, len(word2) - idx2)
            
            total = inf
            
            if word1[idx1] == word2[idx2]:
                total = dp(idx1 + 1, idx2 + 1)
            else:
                total = min(total, dp(idx1 + 1, idx2 + 1))
                total = min(total, dp(idx1 + 1, idx2))
                total = min(total, dp(idx1, idx2 + 1))
                total += 1
            
            memo[(idx1, idx2)] = total
            return total
        
        return dp(0, 0)