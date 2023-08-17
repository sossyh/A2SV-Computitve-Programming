class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        freq = Counter(arr)
        
        for i in freq:
            if i == freq[i]:
                ans = max(ans, i)
        
        return ans
        