class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
         
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0
            
            total = 0
            
            
            if text1[i] == text2[j]:
                total = dp(i+1, j+1) + 1 

            
            else:
                total = max(dp(i, j+1), dp(i+1, j))
                
            
            memo[(i, j)] = total
            return total
        
        return dp(0, 0)