class Solution:
    def splitString(self, s: str) -> bool:
        result = []
        
        def backtrack(idx):
            if idx >= len(s):
                return len(result) >= 2
            
            for i in range(idx, len(s)):
                news = int(s[idx: i + 1])
                if not result or  news + 1 == result[-1]:
                    result.append(news)
                    if backtrack(i + 1):
                        return True
                    result.pop()
                                
            return False
        
        return backtrack(0)
        