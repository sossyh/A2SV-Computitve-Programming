class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(lst, idx):
            if idx >= len(s):
                return True
            for i in range(idx, len(s)):
                news = int(s[idx:i+1])
                if lst[-1] - news == 1:
                    lst.append(news)
                    if backtrack(lst, i+1):
                        return True
                    lst.pop()
            return False                   
                        
            
        for i in range(len(s)-1):
            news = int(s[:i+1])
            if backtrack([news], i+1):
                return True
        return False
    
        