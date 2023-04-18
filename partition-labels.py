class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        
        size = 0
        end = 0
        result = []
        
        for j in range(len(s)):

            end = max(end,last[s[j]])
            size += 1
            if j == end:
                result.append(size)
                size = 0
        return result