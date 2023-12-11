class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Problem: input - s, t - strings
                 output - boolean if s is a subsequence of t
        
        Solution:
                1. will explore every subsequence using backtracking (memoize) - DP
                2. chech if there is a match
        
        backtarcking
        1. states - (idx)
        2. basecase - if idx >= len(t)
        3. recurence relation - calling the function with idx + 1   
        
        """
        if s == "":
            return True

        sp, tp = 0, 0

        while tp < len(t):
            print(sp, tp)
            if s[sp] != t[tp]:
                tp += 1
            
            else:
                sp += 1
                tp += 1
            
            if sp == len(s):
                break
        
        return sp >= len(s)



