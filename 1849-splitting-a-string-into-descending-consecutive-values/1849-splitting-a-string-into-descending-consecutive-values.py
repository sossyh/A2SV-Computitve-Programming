class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(lst, idx):
            if idx > len(s) - 1:
                return True
            for i in range(idx, len(s)):
                newss = s[idx : i + 1]
                if (lst[-1] - int(newss)) == 1:
                    lst.append(int(newss))
                    if backtrack(lst, i + 1):
                        return True  
                    lst.pop()
        
        
        for i in range(len(s)-1):
            news = int(s[:i + 1])
            if backtrack([news], i+1):
                return True
        return False
            
        