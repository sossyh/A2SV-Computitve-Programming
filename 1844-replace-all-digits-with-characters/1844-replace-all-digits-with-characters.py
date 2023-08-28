class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        
        for i in range(len(s)):
            if i % 2 == 0:
                ans += s[i]
            else:
                a = ord(s[i-1]) + int(s[i])
                ans += chr(a)
        
        return ans