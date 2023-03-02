class Solution:
    def isPalindrome(self, s: str) -> bool:
        palic = ""
        
        for i in s:
            if i.isalnum():
                palic += i
                
        palo=palic.lower()
        
        l = 0
        r = len(palic)-1
        while l < r:
            if palo[l] != palo[r]:
                return False
            
            l += 1
            r -= 1
            
        return True