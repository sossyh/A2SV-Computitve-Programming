class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        start = 0
        count, window = Counter(t), {}
        have, need = 0, len(count)
        result, resl = [-1, -1], inf
        
        for end in range(len(s)):
            c = s[end]
            window[c] = 1 + window.get(c, 0)
            
            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                if (end - start + 1) < resl:
                    result = [start, end]
                    resl = end - start + 1
                m = s[start]
                window[m] -= 1
                if m in count and window[m] < count[m]:
                    have -= 1
                if window[m] == 0:
                    del window[m]
                
                start += 1
        
        l, r = result[0], result[1]
            
        return s[l: r + 1] if resl != inf else ""
        