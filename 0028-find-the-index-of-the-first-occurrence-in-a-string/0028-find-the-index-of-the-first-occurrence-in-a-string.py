class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        index = inf
        
        start = 0
        
        for end in range(len(haystack)):
            
            if end >= len(needle):
                start += 1
                
            if haystack[start: end + 1] == needle and start < index:
                index = start
        
        return index if index != inf else -1
                