class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        d = {}
        match = 0
        for i in s1:
            if i not in d:
                d[i] = 0
            d[i] += 1
        
        for end in range(len(s2)):
            last = s2[end]
            if last in d:
                d[last] -= 1
                if d[last] == 0:
                    match += 1
            if match == len(d):
                return True
            if end >= len(s1) - 1:
                first = s2[start]
                if first in d:
                    if d[first] == 0:
                        match -= 1
                    d[first] += 1
                start += 1
                
        return False
    
