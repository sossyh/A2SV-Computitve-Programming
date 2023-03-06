class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = {}
        for i in p:
            if i not in dp:
                dp[i] = 0
            dp[i] += 1
        
        start = 0
        result = []
        match = 0
        
        for end in range(len(s)):
            last = s[end]
            if last in dp:
                dp[last] -= 1
                if dp[last] == 0:
                    match += 1
            if match == len(dp):
                result.append(start)
                    
            if end >= len(p) - 1:
                first = s[start]
                start += 1
                if first in dp:
                    if dp[first] == 0:
                        match -= 1
                    dp[first] += 1
                
        
        return result
                    
                    
                
        