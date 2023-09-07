class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = Counter(arr)
        
        maxf = 0
        ans = None
        
        for i in freq:
            if freq[i] > maxf:
                maxf = freq[i]
                ans = i
        
        return ans
        