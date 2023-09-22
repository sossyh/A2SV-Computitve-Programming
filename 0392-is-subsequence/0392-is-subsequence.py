class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        sp, tp = 0, 0
        same = 0
        
        while tp < len(t):
            if sp > len(s) - 1:
                break
                
            if s[sp] == t[tp]:
                same += 1
                sp += 1
                
            tp += 1
        
        
        return same == len(s)