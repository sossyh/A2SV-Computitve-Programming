class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        
        for i in s:
            if ord(i) < 91 and ord(i) >= 65:
                ans += chr(ord(i)+32)
            else:
                ans += i
        
        return ans
                
        