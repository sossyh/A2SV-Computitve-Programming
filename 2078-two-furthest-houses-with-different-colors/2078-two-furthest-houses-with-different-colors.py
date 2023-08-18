class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        l, r = 0, len(colors) - 1
        
        while l < r:
            if colors[l] == colors[r]:
                r -= 1
            else:
                ans = max(ans, r - l)
                break
        
        r = len(colors) - 1
        while l < r:
            if colors[l] == colors[r]:
                l += 1
            else:
                ans = max(ans, r - l)
                break
                
                
        return ans