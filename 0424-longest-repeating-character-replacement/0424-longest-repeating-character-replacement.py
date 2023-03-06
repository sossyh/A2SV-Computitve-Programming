class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = maxCount = 0
        max_ = float("-inf")
        freq = Counter()
        for end in range(len(s)):
            freq[s[end]] += 1
            maxCount = max(maxCount, freq[s[end]])
            while (end - start + 1) - maxCount > k:
                freq[s[start]] -= 1
                start += 1
            max_ = max(max_, end-start + 1)
        return max_
                
            
            
                    
            