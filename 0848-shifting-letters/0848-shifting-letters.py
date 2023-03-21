class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sums = 0
        n = len(s)
        prefix = [0] * n
        currsum = 0
        ans = ""
        
        for i in range(n):
            currsum += shifts[-1-i]
            prefix[-1-i] = currsum
        
        for i in range(n):
            a = (((ord(s[i]) + prefix[i]) - 97) % 26) + 97
            ans += chr(a)
        
        return ans
        
        
            
            
        