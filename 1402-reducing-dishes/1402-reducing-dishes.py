class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        ans = 0
        satisfaction.sort(reverse = True)
        total = 0
        
        for i in range(len(satisfaction)):
            total += satisfaction[i]
            ans = max(total+ans, ans)
        
        return ans