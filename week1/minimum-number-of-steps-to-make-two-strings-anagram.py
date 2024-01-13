class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)
        result = 0

        for char in sc:
            if char in tc:
                if tc[char] == sc[char]:
                    
                    result += tc[char]
                else:
                    
                    result += min(sc[char], tc[char])
        
        return len(t) - result