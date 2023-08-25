class Solution:
    def maxScore(self, s: str) -> int:
        left = ""
        right = s
        ans = -inf
        
        for i in range(len(s)-1):
            left += s[i]
            right = s[i+1:]
            cl = left.count('0')
            cr = right.count('1')
            ans = max(ans, cl+cr)
        
        return ans