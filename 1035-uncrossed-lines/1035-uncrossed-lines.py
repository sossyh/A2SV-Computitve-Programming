class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            total = 0
            
            
            if nums1[i] == nums2[j]:
                total = dp(i+1, j+1) + 1 
            
            else:
                total = max(dp(i, j+1), dp(i+1, j))
            
            memo[(i, j)] = total
            return total
        
        return dp(0, 0)
        