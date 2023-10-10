class Solution:
    def lps_list(self, p):
        lps = [0] * len(p)
        i = 0

        for j in range(1, len(p)):
            while i and p[i] != p[j]:
                i = lps[i - 1]

            if p[i] == p[j]:
                i += 1
                lps[j] = i
                
        return lps
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        lps = self.lps_list(needle)
        
        pattern_i = 0
        
        for j in range(len(haystack)):
            while pattern_i and haystack[j] != needle[pattern_i]:
                pattern_i = lps[pattern_i - 1]
            
            if haystack[j] == needle[pattern_i]:
                
                if pattern_i == len(needle) - 1:
                    return j + 1 - len(needle) 
                
                pattern_i += 1
        
        return -1