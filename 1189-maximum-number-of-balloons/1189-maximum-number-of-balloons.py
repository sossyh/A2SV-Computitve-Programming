class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        
        expected = Counter(text)
        ans = inf
        
        for i in expected:
            if i in balloon:
                a = expected[i] // balloon[i]
                ans = min(ans, a)
                
        return 0 if ans == inf or len(expected) < len(balloon) else ans
        
        