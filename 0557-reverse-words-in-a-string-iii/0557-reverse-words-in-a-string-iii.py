class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reversedchars = []
        
        for i in s:
            reversedchars.append(i[::-1])
        
        return " ".join(reversedchars)