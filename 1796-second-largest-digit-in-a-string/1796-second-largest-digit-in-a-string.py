class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        
        for i in s:
            if i.isdigit():
                digits.add(int(i))
        
        if len(digits) <= 1:
            return -1
        
        fmax, smax = -inf, -inf
        
        for i in digits:
            if i > fmax:
                smax = fmax
                fmax = i                
            elif i < fmax and i > smax:
                smax = i
        
        return smax