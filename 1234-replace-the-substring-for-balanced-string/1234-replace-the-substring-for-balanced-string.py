class Solution:    
    def isbalanced(self, freq, comp):
        for i in freq:
            if freq[i] > comp:
                return False
        
        return True
    
    def balancedString(self, s: str) -> int:
        min_ = float("inf")
        start = 0
        freq = Counter(s)
        n = len(s) // 4
        
        for end in range(len(s)):
            freq[s[end]] -= 1
            
            while start < len(s) and self.isbalanced(freq, n):
                min_ = min(min_, end - start + 1)
                freq[s[start]] += 1
                start += 1
            
        
        return min_