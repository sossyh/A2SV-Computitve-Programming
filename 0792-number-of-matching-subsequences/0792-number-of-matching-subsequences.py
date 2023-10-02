class Solution:   
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dp = [[-1 for i in range(26)] for i in range(len(s)+1)]
        
        for i in range(len(s)-1, -1, -1):
            element = s[i]
            idx = ord(element) - ord('a')
            a = dp[i+1].copy()
            a[idx] = i
            dp[i] = a
        
        
        count = 0
        
        for word in words:
            j = 0
            notoccured = False
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                if i < len(word) and dp[j][idx] == -1:
                    notoccured = True
                j = dp[j][idx] + 1
            
            if not notoccured:
                count += 1
        
        return count
                
            
        