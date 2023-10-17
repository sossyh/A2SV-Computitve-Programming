class Solution:
    def expand(self, i, j, s):
        
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return [i + 1, j]
            
    def longestPalindrome(self, s: str) -> str:
        
        max_ptr = [0, 0]
        
        for i in range(len(s)):
            first = self.expand(i, i, s)
            second = self.expand(i, i + 1, s)
            curr = 0
          
            if first[1] - first[0] > second[1] - second[0]:
                curr = first
            else:
                curr = second
            
            
            if max_ptr[1] - max_ptr[0] < (curr[1]) - (curr[0]):
                max_ptr = curr
            
        return s[max_ptr[0]: max_ptr[1]]
            
            