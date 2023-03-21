class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * n
        ords = 0
        ans = ""
        
        for start, end, direction in shifts:
            if direction == 0:
                prefix[start] -= 1
                if end + 1 < n:
                    prefix[end + 1] += 1
            if direction == 1:
                prefix[start] += 1
                if end + 1 < n:
                    prefix[end + 1] -= 1
        curr = 0
        for i in range(n):
            curr += prefix[i]
            a = (((curr + ord(s[i])) - 97)  % 26) + 97
            ans += (chr(a))
            
        return ans
                
            
            
            