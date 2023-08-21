class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 1
            
        total = 0
        for i in range(len(s)):
            prefix = s[:i+1]
            if (prefix == '0' or prefix[0] != '0') and int(prefix) > 0 and int(prefix) <= 26:
                res = self.numDecodings(s[i+1:])
                total += res

        return total
        
        
                    