class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_ = float("-inf")
        d = {}
        
        for end in range(len(s)):
            last = s[end]
            if last not in d:
                d[last] = 0
            else:
                while last in d:
                    del d[s[start]]
                    start += 1
                d[last] = 0
            max_ = max(max_, end -start + 1)
        
        return max_ if max_ != float("-inf") else 0
        