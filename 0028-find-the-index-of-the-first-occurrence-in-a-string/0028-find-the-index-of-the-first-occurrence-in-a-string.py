class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        a = len(needle)
        k = a
        needles_hash = 0
        
        for i in needle:
            needles_hash += (ord(i) - 96) * (27 ** (k - 1))
            # needles_hash %= (10**9 + 7)
            k -= 1
        
        curr_hash = 0
        start = 0
        
        for end in range(len(needle)):
            i = haystack[end]
            curr_hash = (curr_hash * 27) + (ord(i) - 96)
            
        if needles_hash == curr_hash:
                return start
            
        for end in range(len(needle), len(haystack)):
            i = haystack[end]
            curr_hash = (curr_hash * 27) + (ord(i) - 96)
            
            
            j = ord(haystack[start]) - 96
            curr_hash -= (j * (27 ** (a))) 
            start += 1
                
            if needles_hash == curr_hash:
                return start
        
        return -1